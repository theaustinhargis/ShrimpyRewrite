import discord
from discord.ext import commands


class Moderation(commands.Cog):

    moderation = discord.SlashCommandGroup(name="moderate", description="A group of all moderation related commands")

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ban_user", description="Bans a specified user")
    async def ban_user(self, ctx, user: discord.Member):
        pass

    @commands.slash_command(name="unban_user", description="Unbans a specified user")
    async def unban_user(self, ctx, user: discord.Member):
        pass

    @commands.slash_command(name="kick_user", description="Kicks a specified user")
    @commands.has_permissions(kick_members=True)
    async def kick_user(self, ctx, user: discord.Member, reason: discord.SlashCommandOptionType.string):
        await ctx.guild.kick(user, reason=reason)
        await ctx.respond(f"Member {user} has been kicked.")

    @commands.slash_command(name="mute_user", description="Mutes a specified user")
    async def mute_user(self, ctx, user: discord.Member):
        pass

    @commands.slash_command(name="unmute_user", description="Unmutes a specified user")
    async def unmute_user(self, ctx, user: discord.Member):
        pass


def setup(bot):
    bot.add_cog(Moderation(bot))
