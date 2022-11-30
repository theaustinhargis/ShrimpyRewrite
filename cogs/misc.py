import discord
from discord.ext import commands


class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="about", description="Provides information about Shrimpy")
    async def about(self, ctx):
        embed = discord.Embed(
            title="Shrimpy",
            description="Version: 0.2.0a",
            color=discord.Color.blurple()
        )

        embed.add_field(name="About Shrimpy", value="Shrimpy originally began development in March of 2021. The backend for Shrimpy has been through several revisions due to changing Discord APIs. However, pycord seems to be a stable and well-supported open-source API, so Shrimpy should be able to stick around from here on out.", inline=False)
        embed.add_field(name="Technology", value="Shrimpy is written in Python 3.11 with Pycord v2.3.0.")
        embed.add_field(name="GitHub", value='[https://github.com/theaustinhargis/ShrimpyRewrite](https://github.com/theaustinhargis/ShrimpyRewrite)')
        embed.set_author(name="Austin Hargis", icon_url='https://avatars.githubusercontent.com/u/25471876?v=4')
        embed.set_footer(text="Created by Austin Hargis & Contributors - 09/29/22")

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Misc(bot))
