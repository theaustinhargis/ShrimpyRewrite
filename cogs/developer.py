import os

import discord
from discord.ext import commands


class Developer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="latency", description="Returns Shrimpy's latency")
    async def latency(self, ctx):
        await ctx.respond(f'Current latency is {self.bot.latency:.2f}ms')

    @commands.slash_command(name="reload_extension", description="Reloads specified extension")
    async def reload_cog(self, ctx, extension: discord.Option(discord.SlashCommandOptionType.string, description="An extension for Shrimpy")):
        if ctx.author.id == int(os.getenv('OWNER')):
            self.bot.reload_extension(f'cogs.{extension}')
            await ctx.respond(f'Reloaded cog.{extension}')
        else:
            await ctx.respond(f'You don\'t have permission to use this command.')

    @commands.slash_command(name="load_extension", description="Loads specified extension")
    async def load_cog(self, ctx, extension: discord.Option(discord.SlashCommandOptionType.string, description="An extension for Shrimpy")):
        try:
            if ctx.author.id == int(os.getenv('OWNER')):
                self.bot.load_extension(f'cogs.{extension}')
                await ctx.respond(f'Loaded cog.{extension}')
            else:
                await ctx.respond(f'You don\'t have permission to use this command.')
        except discord.ExtensionAlreadyLoaded:
            await ctx.respond(f'Cog {extension} is already loaded.')
        except discord.ExtensionNotFound:
            await ctx.respond(f'Cog {extension} was not found, please try again.')

    @commands.slash_command(name="unload_extension", description="Unloads specified extension")
    async def unload_cog(self, ctx, extension: discord.Option(discord.SlashCommandOptionType.string, description="An extension for Shrimpy")):
        try:
            if ctx.author.id == int(os.getenv('OWNER')):
                self.bot.unload_extension(f'cogs.{extension}')
                await ctx.respond(f'Unloaded cog.{extension}')
            else:
                await ctx.respond(f'You don\'t have permission to use this command.')
        except discord.ExtensionAlreadyLoaded:
            await ctx.respond(f'Cog {extension} is already loaded.')
        except discord.ExtensionNotFound:
            await ctx.respond(f'Cog {extension} was not found, please try again.')


def setup(bot):
    bot.add_cog(Developer(bot))
