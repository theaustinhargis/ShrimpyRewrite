import datetime
import discord
from discord.ext import commands


class Moderation(commands.Cog):

    moderation = discord.SlashCommandGroup(name="moderate", description="A group of all moderation related commands")

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ban_user", description="Bans a specified user")
    @commands.has_permissions(ban_members=True)
    async def ban_user(self, ctx, user: discord.Member, reason: discord.Option(discord.SlashCommandOptionType.string, required=False)):
        await ctx.guild.ban(user, reason=reason)
        await ctx.respond(f"Member {user} has been banned.")

    @commands.slash_command(name="unban_user", description="Unbans a specified user")
    @commands.has_permissions(ban_members=True)
    async def unban_user(self, ctx, user: discord.Member, reason: discord.Option(discord.SlashCommandOptionType.string, required=False)):
        await ctx.guild.unban(user, reason=reason)
        await ctx.respond(f"Member {user} has been unbanned.")

    @commands.slash_command(name="kick_user", description="Kicks a specified user")
    @commands.has_permissions(kick_members=True)
    async def kick_user(self, ctx, user: discord.Member, reason: discord.Option(discord.SlashCommandOptionType.string, required=False)):
        await ctx.guild.kick(user, reason=reason)
        await ctx.respond(f"Member {user} has been kicked.")

    @commands.slash_command(name="timeout_user", description="Puts the specified user in timeout")
    @commands.has_permissions(moderate_members=True)
    async def mute_user(self, ctx, time: discord.Option(int, name="minutes", required=True), user: discord.Member, reason: discord.Option(discord.SlashCommandOptionType.string, required=False)):
        await user.timeout_for(datetime.timedelta(minutes=time), reason=reason)
        await ctx.respond(f"Member <@{user.id}> was put in timeout.")

    @commands.slash_command(name="remove_timeout", description="Removes the specified user from timeout")
    @commands.has_permissions(moderate_members=True)
    async def unmute_user(self, ctx, user: discord.Member):
        await user.remove_timeout()
        await ctx.respond(f"Member <@{user.id}> was removed from timeout.")


def setup(bot):
    bot.add_cog(Moderation(bot))
