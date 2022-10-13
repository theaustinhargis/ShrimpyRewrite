import discord
from discord.ext import commands


class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ban_user", description="Bans a specified user")
    async def ban_user(self, ctx, user: discord.Member):
        pass

    @commands.slash_command(name="unban_user", description="Unbans a specified user")
    async def unban_user(self, ctx, user: discord.Member):
        pass

    @commands.slash_command(name="kick_user", description="Kicks a specified user")
    async def kick_user(self, ctx, user: discord.Member):
        pass

    @commands.slash_command(name="mute_user", description="Mutes a specified user")
    async def mute_user(self, ctx, user: discord.Member):
        pass

    @commands.slash_command(name="unmute_user", description="Unmutes a specified user")
    async def unmute_user(self, ctx, user: discord.Member):
        pass


def setup(bot):
    bot.add_cog(Moderation(bot))
