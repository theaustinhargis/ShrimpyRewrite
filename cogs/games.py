import random

import discord
from discord.ext import commands


class Games(commands.Cog):

    games = discord.SlashCommandGroup(name="games", description="A group of Shrimpy's games")

    def __init__(self, bot):
        self.bot = bot

    @games.command(name="ping", description="Play virtual ping-pong with Shrimpy")
    async def ping(self, context):
        await context.respond(f"Pong!")

    @games.command(name="random", description="Get a random number generated for you (defaults to 100 num2 isn't specified)")
    async def randomnum(self, context, num1: discord.Option(discord.SlashCommandOptionType.integer), num2: discord.Option(discord.SlashCommandOptionType.integer, required=False)):
        if num2 is None:
            num2 = 100
        randnum = random.randint(num1, num2)
        await context.respond(f"Your random number between {num1} and {num2} is {randnum}!")

    @games.command(name="shrimp", description="Shrimp a random person, or, if you\'re feeling extra spicy, shrimp someone specific.")
    async def shrimp(self, context, user: discord.Option(discord.Member, description='user', required=False)):

        if user is not None:
            user_id = user.id
        else:
            ids = [user.id for user in context.channel.members]
            user_id = random.choice(ids)

        await context.respond(f"\U0001F364 Congrats <@{user_id}>, you have been shrimped! \U0001F364")


def setup(bot):
    bot.add_cog(Games(bot))
