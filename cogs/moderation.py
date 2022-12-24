import datetime
import discord
from discord.ext import commands


class Moderation(commands.Cog):

    moderation = discord.SlashCommandGroup(name="moderate", description="A group of all moderation related commands")

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ban_user", description="Bans a specified user")
    @commands.has_permissions(ban_members=True)
    async def ban_user(self, context, user: discord.Member, reason: discord.Option(discord.SlashCommandOptionType.string, required=False)):
        await context.guild.ban(user, reason=reason)
        await context.respond(f"Member {user} has been banned.")

    @commands.slash_command(name="unban_user", description="Unbans a specified user")
    @commands.has_permissions(ban_members=True)
    async def unban_user(self, context, user: discord.Member, reason: discord.Option(discord.SlashCommandOptionType.string, required=False)):
        await context.guild.unban(user, reason=reason)
        await context.respond(f"Member {user} has been unbanned.")

    @commands.slash_command(name="kick_user", description="Kicks a specified user")
    @commands.has_permissions(kick_members=True)
    async def kick_user(self, context, user: discord.Member, reason: discord.Option(discord.SlashCommandOptionType.string, required=False)):
        await context.guild.kick(user, reason=reason)
        await context.respond(f"Member {user} has been kicked.")

    @commands.slash_command(name="timeout_user", description="Puts the specified user in timeout")
    @commands.has_permissions(moderate_members=True)
    async def mute_user(self, context, time: discord.Option(int, name="minutes", required=True), user: discord.Member, reason: discord.Option(discord.SlashCommandOptionType.string, required=False)):
        await user.timeout_for(datetime.timedelta(minutes=time), reason=reason)
        await context.respond(f"Member <@{user.id}> was put in timeout.")

    @commands.slash_command(name="remove_timeout", description="Removes the specified user from timeout")
    @commands.has_permissions(moderate_members=True)
    async def unmute_user(self, context, user: discord.Member):
        await user.remove_timeout()
        await context.respond(f"Member <@{user.id}> was removed from timeout.")

    # TODO: Implement purge messages command
    @commands.slash_command(name="purge", description="Purges a specified amount of comments from the current channel")
    @commands.has_permissions(manage_messages=True)
    async def purge_messages(self, context, message_count: int):
        count = 0
        async for message in context.channel.history(limit=message_count):
            if count > 0:
                await message.delete(delay=1)
            count += 1
        await context.respond(f"I have deleted the {message_count} most recent message(s).")


def setup(bot):
    bot.add_cog(Moderation(bot))
