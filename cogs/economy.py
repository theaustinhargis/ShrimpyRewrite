import discord
from discord.ext import commands


class Economy:

    economy = discord.SlashCommandGroup(name="economy", description="A group of Shrimpy Economy commands")

    def __init__(self, bot):
        self.bot = bot

    # TODO: implement check balance command
    @economy.command(name="balance", description="Returns your Shrimpy Economy balance")
    async def check_balance(self, context):
        pass

    # TODO: implement transfer balance command
    @economy.command(name="transfer", description="Transfers an amount of your Shrimpy Economy balance to another user")
    async def transfer_balance(self, context, user: discord.Member, amount: discord.SlashCommandOptionType.integer):
        pass

    # TODO: implement paycheck command
    @economy.command(name="paycheck", description="Collect your weekly paycheck, if one is available")
    async def paycheck(self):
        pass


def setup(bot):
    bot.add_cog(Economy(bot))
