import discord
from dotenv import load_dotenv
import logging
import os

cogs_list = [
    'greetings'
]

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv()

bot = discord.Bot()

@bot.event
async def on_member_join(member):
    await member.send(f'Welcome to the server, {member}. Please enjoy your stay!')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


@bot.slash_command()
async def hello(ctx):
    await ctx.respond('Hello!')

bot.run(os.getenv('TOKEN'))

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')
