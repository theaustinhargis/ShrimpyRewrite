import discord
from discord.ext import commands


class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='about', description='Provides information about Shrimpy')
    async def about(self):
        embed = discord.Embed(
            title='About Shrimpy',
            description='Version: 0.1.0a',
            color=discord.Color.blurple()
        )

        embed.add_field(name='Technology', value='Shrimpy is written in Python 3.10 with Pycord v2.1.1.')
        embed.set_author(name='Austin Hargis')
        embed.set_footer(text='https://github.com/theaustinhargis/ShrimpyRewrite')


def setup(bot):
    bot.add_cog(Misc(bot))
