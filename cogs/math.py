import discord
from discord.ext import commands
import matplotlib.pyplot as plt
import numpy as np


class Math(commands.Cog):

    math = discord.SlashCommandGroup(name="math", description="Mathematic functions")

    def __init__(self, bot):
        self.bot = bot

    @math.command(name="add", description="Add two values together")
    async def add_values(self, context, num_1: int, num_2: int):
        await context.respond(f"The sum of those values is {num_1 + num_2}.")

    @math.command(name="subtract", description="Subtract two values")
    async def subtract_values(self, context, num_1: int, num_2: int):
        await context.respond(f"The difference of those values is {num_1 - num_2}.")

    @math.command(name="multiply", description="Multiply two values")
    async def multiply_values(self, context, num_1: int, num_2: int):
        await context.respond(f"The product of those values is {num_1 * num_2}.")

    @math.command(name="divide", description="Divide two values")
    async def divide_values(self, context, num_1: int, num_2: int):
        try:
            await context.respond(f"The quotient of those values is {num_1/num_2}")
        except ZeroDivisionError:
            await context.respond(f"Zero division is not possible.")

    @math.command(name="exponential", description="Solves an exponential equation")
    async def exponential(self, context, base: float, exponent: float):
        await context.respond(f"The solution to your exponential is {base**exponent}.")

    @math.command(name="factors", description="List factors of an integer")
    async def list_factors(self, context, integer: int):
        factors = []
        msg = f"```\nFactors of {integer}:\n"

        for x in range(1, integer + 1):
            if (integer % x) == 0:
                factors.append(x)
                msg = msg + f"{x} * {integer // x} = {integer}\n"

        msg = msg + f"\n{factors}```"
        await context.respond(msg)

    @math.command(name="graph", description="Graphs a function and returns an image of it")
    async def graph_function(self, context, function: str):
        x = np.array(range(-10, 10))
        y = eval(function)

        plt.plot(x, y)
        plt.savefig('./graph.png')

        file = discord.File("./graph.png", filename="graph.png")

        await context.respond(file=file)


def setup(bot):
    bot.add_cog(Math(bot))
