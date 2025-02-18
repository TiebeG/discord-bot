# discord-bot

This is a simple Discord bot that responds to a slash command to check if the bot is online.

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd discord-bot
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a [.env](http://_vscodecontentref_/1) file in the root directory and add your Discord bot token and server guild ID:
    
```env    DISCORD_BOT_TOKEN="your-bot-token"
    SERVER_GUILD_ID="your-server-guild-id"
    ```

## Running the Bot

To run the bot, use the following command:
```sh
python bot.py