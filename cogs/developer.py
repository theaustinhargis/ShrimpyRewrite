import os

import discord
from discord.ext import commands


class Developer(commands.Cog):

    extensions = discord.SlashCommandGroup(name="extension", description="Group of extension related commands", checks=[commands.is_owner().predicate])

    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, discord.ExtensionAlreadyLoaded):
            await ctx.respond(f'Cog {ctx} is already loaded.')
        elif isinstance(error, discord.ExtensionNotFound):
            await ctx.respond(f'Cog {ctx} was not found, please try again.')
        elif isinstance(error, discord.NoEntryPointError):
            await ctx.respond(f'Cog {ctx} has no setup function. Please correct this or contact the cog\'s developer')
        else:
            await ctx.respond(f'An uncaught error {error} has occured!')
            raise error

    @commands.slash_command(name="latency", description="Returns Shrimpy's latency")
    async def latency(self, ctx):
        await ctx.respond(f'Current latency is {self.bot.latency:.2f}ms')

    @extensions.command(name="reload", description="Reloads specified extension")
    async def reload_cog(self, ctx, extension: discord.Option(discord.SlashCommandOptionType.string, description="An extension for Shrimpy")):
        if ctx.author.id == int(os.getenv('OWNER')):
            self.bot.reload_extension(f'cogs.{extension}')
            await ctx.respond(f'Reloaded cog.{extension}')
        else:
            await ctx.respond(f'You don\'t have permission to use this command.')

    @extensions.command(name="load", description="Loads specified extension")
    async def load_cog(self, ctx, extension: discord.Option(discord.SlashCommandOptionType.string, description="An extension for Shrimpy")):
        if ctx.author.id == int(os.getenv('OWNER')):
            self.bot.load_extension(f'cogs.{extension}')
            await ctx.respond(f'Loaded cog.{extension}')
        else:
            await ctx.respond(f'You don\'t have permission to use this command.')

    @extensions.command(name="unload", description="Unloads specified extension")
    async def unload_cog(self, ctx, extension: discord.Option(discord.SlashCommandOptionType.string, description="An extension for Shrimpy")):
        if ctx.author.id == int(os.getenv('OWNER')):
            self.bot.unload_extension(f'cogs.{extension}')
            await ctx.respond(f'Unloaded cog.{extension}')
        else:
            await ctx.respond(f'You don\'t have permission to use this command.')


def setup(bot):
    bot.add_cog(Developer(bot))
