import base64
import sys
import os
import concurrent.futures
import requests
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field

load_dotenv(override=True)
client = OpenAI(
    api_key=os.environ.get("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def send_slack_notification(message: str) -> None:
    print("Sending Slack notification...")
    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        json={"channel": os.environ.get("CHANNEL_ID"), "text": message},
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ.get('SLACK_ACCESS_TOKEN')}",
        },
    )
    response.raise_for_status()
    data = response.json()
    if data.get("ok"):
        print("Slack notification sent successfully.")
    else:
        raise Exception(f"Failed to send Slack notification: {data.get('error')}")

def generate_motivational_post():
    topic = input("Enter the topic for your motivational post: ")
    prompt = f"""
    Generate a short, inspiring, and motivational post for a team Slack channel.
    The post should be about the following topic: {topic}.
    Keep the tone positive and encouraging. It should be concise and engaging.
    Do not include hashtags or emojis.
    """
    try:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant specialized in writing motivating and encouraging messages for professional teams."
                },
                {"role": "user", "content": prompt}
            ]
        )
        motivational_post = response.choices[0].message.content
        print("\n--- Motivational Post for Slack Team ---")
        print(motivational_post)
        print("\n----------------------------------------")
        send_slack_notification(motivational_post)
    except Exception as e:
        print(f"An error occurred while generating the post: {e}")
        print("Please ensure your API key is correct and the model name is valid for your setup, and that SLACK_ACCESS_TOKEN is set.")

generate_motivational_post()
