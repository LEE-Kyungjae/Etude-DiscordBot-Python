# Simple Discord Bot

This is a basic Discord bot that can be customized for various commands and actions. Discord bots can be developed in multiple languages, including JavaScript, Python, and Java. Each language has its pros and cons, but for simplicity and availability of resources, many developers prefer JavaScript or Python. However, this project is built using **Python**.

## Before You Start

Discord bots can be created in a variety of languages such as JavaScript, Python, and Java. Here's a brief overview of each:
- **JavaScript**: The most common language for Discord bot development with the largest community support.
- **Python**: A great second choice with lots of resources available, though some materials may be outdated due to recent changes in Discord's bot policies.
- **Java**: While possible, it's less common and has fewer resources available.

If you're developing a bot in **Java**, refer to the [JDA (Java Discord API)](https://github.com/discord-jda/JDA) for more information.

## Creating a Discord Bot

To begin, head to the [Discord Developer Portal](https://discord.com/developers/applications) and log in to create your bot application.
1. Click on **New Application** and enter a name for your bot.
2. Assign the bot to a personal team (or leave it as individual).

### Getting the Token
1. Navigate to your bot's settings and find the **Token** section. This token is used to authenticate your bot with Discord.
2. Keep this token secure! It's only shown once, and if you lose it, you'll need to regenerate a new one.

### Adding the Bot to Your Server
1. Go to the **OAuth2** tab and select the **OAuth2 URL Generator**.
2. Under **Scopes**, select `bot`, and then under **Bot Permissions**, choose `Administrator` (or set specific permissions).
3. Copy the generated URL and paste it into your browser to invite your bot to your Discord server.

## Python Setup

### Step 1: Install Python
Download the latest version of Python from [python.org](https://www.python.org/downloads/).

### Step 2: Set Up Your Environment
1. Open your terminal (Command Prompt for Windows or Terminal for macOS/Linux).
2. Use the following commands to install necessary Python modules:
   ```bash
   pip install discord
   pip install asyncio
   pip install requests
   pip install python-dotenv
