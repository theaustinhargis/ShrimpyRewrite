import discord
from discord.ext import commands


class Games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='ping', description='Play virtual ping-pong with Shrimpy')
    async def ping(self, ctx):
        await ctx.respond(f'Pong!')


def setup(bot):
    bot.add_cog(Games(bot))
