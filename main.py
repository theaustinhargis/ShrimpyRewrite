import discord
from dotenv import load_dotenv
import logging
import os

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv()

bot = discord.Bot()


@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error: discord.DiscordException):
    if isinstance(error, discord.ExtensionAlreadyLoaded):
        await ctx.respond(f'Cog {ctx} is already loaded.')
    elif isinstance(error, discord.ExtensionNotFound):
        await ctx.respond(f'Cog {ctx} was not found, please try again.')
    elif isinstance(error, discord.NoEntryPointError):
        await ctx.respond(f'Cog {ctx} has no setup function. Please correct this or contact the cog\'s developer')
    else:
        raise error


@bot.event
async def on_member_join(member):
    await member.send(f'Welcome to the server, {member}. Please enjoy your stay!')


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

    for cog in os.listdir(f'./cogs/'):
        if cog.endswith(f'.py'):
            try:
                bot.load_extension(f'cogs.{cog.replace(".py", "")}')
                print(f'Loaded {cog}')
            except discord.NoEntryPointError:
                print(f'Unable to load {cog} because it has no \'setup\' function')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

bot.run(bot.run(os.getenv('TOKEN')))
