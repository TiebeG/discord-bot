import discord
import os
from discord import app_commands
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Get the bot token from the environment variable
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Enable intents
intents = discord.Intents.default()
intents.message_content = True  # Allows reading message content

# Create bot instance
class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        await self.tree.sync()  # Register commands globally
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f'✅ Bot is online! Logged in as {self.user} since {current_time}')

bot = MyBot()

# Slash command: /online
@bot.tree.command(name="online", description="Check if the bot is online")
async def online(interaction: discord.Interaction):
    await interaction.response.send_message("✅ The bot is online! And I'm ready to serve you!")

# Slash command: /ping
@bot.tree.command(name="ping", description="Check the bot's latency")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Latency: {round(bot.latency * 1000)}ms")

# Slash command: /info
@bot.tree.command(name="info", description="Display general information")
async def info(interaction: discord.Interaction):
    guild = interaction.guild
    embed = discord.Embed(title="Meldkamer Information", color=discord.Color.blue())
    embed.set_thumbnail(url=bot.user.avatar.url if bot.user.avatar else bot.user.default_avatar.url)
    embed.add_field(name="Server Name", value=guild.name, inline=False)
    embed.add_field(name="Bot Status", value=" ✅ Online", inline=True)
    embed.add_field(name="Latency", value=f"{round(bot.latency * 1000)}ms", inline=True)
    embed.add_field(name="Member Count", value=guild.member_count, inline=False)
    embed.set_footer(text="Meldkamer", icon_url=bot.user.avatar.url if bot.user.avatar else bot.user.default_avatar.url)

    await interaction.response.send_message(embed=embed)

# Slash command: /register
@bot.tree.command(name="register", description="Register the server with a code")
async def register(interaction: discord.Interaction, code: int):
    # Placeholder for actual registration logic
    await interaction.response.send_message(f"Server registered with code: {code}")

# Slash command: /subscription
@bot.tree.command(name="subscription", description="Check the subscription status")
async def subscription(interaction: discord.Interaction):
    # Placeholder URL for the Laravel API endpoint
    subscription_status = "Active"
    subscription_days = 30
    if subscription_days >= 1:
        time_left = f"{subscription_days} days"
    else:
        subscription_hours = subscription_days * 24
        if subscription_hours >= 1:
            time_left = f"{int(subscription_hours)} hours"
        else:
            subscription_minutes = subscription_hours * 60
            time_left = f"{int(subscription_minutes)} minutes"
    
    if subscription_status == "Active":
        await interaction.response.send_message(f"Your subscription is still active for {time_left}. Status: {subscription_status}")
    else:
        await interaction.response.send_message(f"Your subscription has expired.")

# Run the bot
bot.run(TOKEN)