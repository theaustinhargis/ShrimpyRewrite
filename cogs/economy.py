import discord
from discord.ext import commands
import sqlite3

db = sqlite3.Connection('./economy.db')
tables = db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
if len(tables) == 0:
    db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, balance INTEGER)")
else:
    pass


class Economy(discord.Cog):

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
    async def paycheck(self, context):
        pass

    @economy.command(name="register", description="Register for the Shrimpy Economy")
    async def register(self, context):
        row = db.execute(f"SELECT * FROM users WHERE id=?", (context.author.id,)).fetchone()

        if row is None:
            db.execute(f'INSERT INTO users (id, balance) VALUES ({context.author.id}, {500})')
            await context.respond(f"Congrats, you have been registered with the Shrimpy Economy. Your starting "
                                  f"balance is $500.")
        else:
            await context.respond(f"You have already registered with the Shrimpy Economy.")

def setup(bot):
    bot.add_cog(Economy(bot))
