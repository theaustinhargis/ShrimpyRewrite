import discord
from discord.ext import commands


class Math(commands.Cog):

    math = discord.SlashCommandGroup(name="math", description="Mathematic functions")

    def __init__(self, bot):
        self.bot = bot

    @math.command(name="add", description="Add two values together")
    async def add_values(self, ctx, num_1: int, num_2: int):
        await ctx.respond(f"The sum of those values is {num_1 + num_2}.")

    @math.command(name="subtract", description="Subtract two values")
    async def subtract_values(self, ctx, num_1: int, num_2: int):
        await ctx.respond(f"The difference of those values is {num_1 - num_2}.")

    @math.command(name="multiply", description="Multiply two values")
    async def multiply_values(self, ctx, num_1: int, num_2: int):
        await ctx.respond(f"The product of those values is {num_1 * num_2}.")

    @math.command(name="divide", description="Divide two values")
    async def divide_values(self, ctx, num_1: int, num_2: int):
        try:
            await ctx.respond(f"The quotient of those values is {num_1/num_2}")
        except ZeroDivisionError:
            await ctx.respond(f"Zero division is not possible.")

    @math.command(name="exponential", description="Solves an exponential equation")
    async def exponential(self, ctx, base: float, exponent: float):
        await ctx.respond(f"The solution to your exponential is {base**exponent}.")

    @math.command(name="factors", description="List factors of an integer")
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
