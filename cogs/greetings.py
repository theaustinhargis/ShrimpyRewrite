import discord
from discord.ext import commands


class Greetings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="hello", description="Tells Shrimpy to say \"Hello!\"")
    async def hello(self, context):
        await context.respond(f"Hello!")


def setup(bot):
    bot.add_cog(Greetings(bot))
