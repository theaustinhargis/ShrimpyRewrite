import os
import sys
import discord
from discord.ext import commands


class Developer(commands.Cog):

    extensions = discord.SlashCommandGroup(name="extension", description="Group of extension related commands", checks=[commands.is_owner().predicate])

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="latency", description="Returns Shrimpy's latency")
    async def latency(self, context):
        await context.respond(f"Current latency is {self.bot.latency:.1f}ms")

    @extensions.command(name="reload", description="Reloads specified extension")
    async def reload_cog(self, context, extension: discord.Option(discord.SlashCommandOptionType.string, description="An extension for Shrimpy")):
        if context.author.id == int(os.getenv('OWNER')):
            self.bot.reload_extension(f'cogs.{extension}')
            await context.respond(f"Reloaded cog.{extension}")
        else:
            await context.respond(f"You don\'t have permission to use this command.")

    @extensions.command(name="load", description="Loads specified extension")
    async def load_cog(self, context, extension: discord.Option(discord.SlashCommandOptionType.string, description="An extension for Shrimpy")):
        if context.author.id == int(os.getenv('OWNER')):
            self.bot.load_extension(f'cogs.{extension}')
            await context.respond(f"Loaded cog.{extension}")
        else:
            await context.respond(f"You don\'t have permission to use this command.")

    @extensions.command(name="unload", description="Unloads specified extension")
    async def unload_cog(self, context, extension: discord.Option(discord.SlashCommandOptionType.string, description="An extension for Shrimpy")):
        if context.author.id == int(os.getenv('OWNER')):
            self.bot.unload_extension(f'cogs.{extension}')
            await context.respond(f"Unloaded cog.{extension}")
        else:
            await context.respond(f"You don't have permission to use this command.")

    @extensions.command(name="list", description="Lists all extensions in Shrimpy's directory")
    async def list_cog(self, context):
        if context.author.id == int(os.getenv('OWNER')):
            msg = "```Here's a list of all of Shrimpy's extensions.\n" \
                  "Please note that an extension being listed here does not mean it is configured in a way that allows " \
                  "it to be loaded.\n\n"
            for file in sorted(os.listdir('./cogs')):
                if file.endswith('.py'):
                    msg = msg + file + "\n"
            msg = msg + "```"
            await context.respond(msg)
        else:
            await context.respond(f"You don't have permission to use this command.")

    @extensions.command(name="shutdown", description="Issues a shutdown command to Shrimpy")
    async def shutdown(self, context):
        if context.author.id == int(os.getenv('OWNER')):
            sys.exit()


def setup(bot):
    bot.add_cog(Developer(bot))
