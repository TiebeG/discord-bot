import discord
from discord import app_commands
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the bot token from the environment variable
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

GUILD_ID = os.getenv('DISCORD_GUILD_ID')  # Replace with your server ID

# Enable intents
intents = discord.Intents.default()
intents.message_content = True  # Allows reading message content

# Create bot instance
class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        await self.tree.sync(guild=discord.Object(id=GUILD_ID))  # Register commands
        print(f'✅ Bot is online! Logged in as {self.user}')

bot = MyBot()

# Slash command: /online
@bot.tree.command(name="online", description="Check if the bot is online", guild=discord.Object(id=GUILD_ID))
async def online(interaction: discord.Interaction):
    await interaction.response.send_message("✅ The bot is online!")

# Run the bot
bot.run(TOKEN)

