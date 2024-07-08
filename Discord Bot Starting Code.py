#pip install discord.py

import discord
from discord.ext import commands

# Initialize Discord bot with command prefix
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

#Bot will go online in server and write "online" in specified channel
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    bota_channel = bot.get_channel('PUT YOUR CHANNEL ID HERE')
    if bota_channel:
        await bota_channel.send("online")

#Bot will ignore its own messages and messages not in the specified channel
@bot.event
async def on_message(message):
    if message.author == bot.user:
        if message.channel.id == 'PUT YOUR CHANNEL ID HERE':
            return


# Run the bot with your bot token
bot.run('PUT YOUR BOT ID HERE')