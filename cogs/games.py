import random

import discord
from discord.ext import commands


class Games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='ping', description='Play virtual ping-pong with Shrimpy')
    async def ping(self, ctx):
        await ctx.respond(f'Pong!')

    @commands.slash_command(name='randomnum', description='Get a random number generated for you')
    async def randomnum(self, ctx, num1: discord.Option(discord.SlashCommandOptionType.integer), num2: discord.Option(discord.SlashCommandOptionType.integer)):
        randnum = random.randint(num1, num2)
        await ctx.respond(f'Your random number between {num1} and {num2} is {randnum}!')

def setup(bot):
    bot.add_cog(Games(bot))
