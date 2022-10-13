import discord
from discord.ext import commands


class Math(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="add_values", description="Add values together")
    async def add_values(self, ctx, int1: int, int2: int):
        await ctx.respond(f"The sum of those values is {int1+int2}.")

    @commands.slash_command(name="subtract_values", description="Subtract values")
    async def subtract_values(self, ctx, int1: int, int2: int):
        await ctx.respond(f"The difference of those values is {int1-int2}.")

    @commands.slash_command(name="multiply_values", description="Multiply values")
    async def multiply_values(self, ctx, int1: int, int2: int):
        await ctx.respond(f"The product of those values is {int1*int2}.")

    @commands.slash_command(name="divide_valies", description="Divide values")
    async def divide_values(self, ctx, int1: int, int2: int):
        await ctx.respond(f"The quotient of those values is {int1/int2}")

    @commands.slash_command(name="exponential", description="Solves an exponential equation")
    async def exponential(self, ctx, base: float, exponent: float):
        await ctx.respond(f"The solution to your exponential is {base**exponent}.")

    @commands.slash_command(name="list_factors", description="List factors of an integer")
    async def list_factors(self, ctx, integer: int):
        factors = []
        msg = f"```\nFactors of {integer}:\n"

        for x in range(1, integer + 1):
            if (integer % x) == 0:
                factors.append(x)
                msg = msg + f"{x} * {integer // x} = {integer}\n"

        msg = msg + f"\n{factors}```"
        await ctx.respond(msg)


def setup(bot):
    bot.add_cog(Math(bot))