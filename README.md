AI-Powered Slack Motivational Post Generator
This Python script uses Google's Gemini AI to generate and automatically post motivational messages to your team's Slack channel.

🚀 Quick Start in Google Colab
This code is ready to run in Google Colab. Simply set up your API keys properly and execute.

⚙️ Setup & Configuration
Prerequisites: Create a .env file with these variables:

text
GEMINI_API_KEY=your_google_ai_studio_key
SLACK_ACCESS_TOKEN=your_slack_bot_oauth_token
CHANNEL_ID=your_slack_channel_id
Get these keys from Google AI Studio and Slack API dashboard. Demo available in accompanying tutorial video.

📋 How It Works
User Input: Enter a topic when prompted (e.g., "weekly goals")

AI Generation: Gemini AI creates a concise, encouraging message

Auto-Post: Message delivers automatically to your Slack channel

✨ Features
Generates context-aware motivational posts

Eliminates manual Slack posting

Secure credential management via environment variables

🛠 Technology Stack
Python, openai library (Gemini API), requests (Slack API), python-dotenv

🔧 Setup Requirements
Google AI Studio API key

Slack Bot Token with chat:write permission

Target Slack Channel ID

