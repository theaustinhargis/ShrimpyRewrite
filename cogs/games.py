import random

import discord
from discord.ext import commands


class Games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='ping', description='Play virtual ping-pong with Shrimpy')
    async def ping(self, ctx):
        await ctx.respond(f'Pong!')

    @commands.slash_command(name='randomnum', description='Get a random number generated for you')
    async def randomnum(self, ctx, num1: discord.Option(discord.SlashCommandOptionType.integer), num2: discord.Option(discord.SlashCommandOptionType.integer)):
        randnum = random.randint(num1, num2)
        await ctx.respond(f'Your random number between {num1} and {num2} is {randnum}!')

    @commands.slash_command(name='shrimp', description='Shrimp a random person, or, if you\'re feeling extra spicy, shrimp someone specific.')
    async def shrimp(self, ctx, user: discord.Option(discord.Member, description='user', required=False)):

        print(user)

        if user is not None:
            user_id = user.id
        else:
            ids = [user.id for user in ctx.channel.members]
            user_id = random.choice(ids)

        await ctx.respond(f'\U0001F364 Congrats <@{user_id}>, you have been shrimped! \U0001F364')


def setup(bot):
    bot.add_cog(Games(bot))
