from datetime import datetime
import discord
import sqlite3

db = sqlite3.Connection('./economy.db')
tables = db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
if len(tables) == 0:
    db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, balance INTEGER, last_paycheck INTEGER)")


class Economy(discord.Cog):
    economy = discord.SlashCommandGroup(name="economy", description="A group of Shrimpy Economy commands")

    def __init__(self, bot):
        self.bot = bot

    @economy.command(name="balance", description="Returns your Shrimpy Economy balance")
    async def check_balance(self, context):
        row = db.execute(f"SELECT * FROM users WHERE id={context.author.id}").fetchone()
        if row is not None:
            await context.respond(f"Hello <@{context.author.id}>! Your current balance is ${row[1]}.")
        else:
            await context.respond(f"Hello <@{context.author.id}>. It appears that you do not have an account. In order "
                                  f"to use economy features, please run the '/economy register' command.")

    @economy.command(name="transfer", description="Transfers an amount of your Shrimpy Economy balance to another user")
    async def transfer_balance(self, context, amount: discord.SlashCommandOptionType.integer, user: discord.Member):
        target_row = db.execute(f"SELECT * FROM users WHERE id=?", (user.id,)).fetchone()
        if target_row is not None:
            from_row = db.execute(f'SELECT * FROM users WHERE id=?', (context.author.id,)).fetchone()
            if from_row[1] >= amount:
                db.execute(f'UPDATE users SET balance = {from_row[1] - amount} WHERE id = {context.author.id}')
                db.execute(f'UPDATE users SET balance = {from_row[1] + amount} WHERE id = {user.id}')
                await context.respond(f"You have successfully transferred ${amount} to <@{user.id}>")
            else:
                await context.respond(f"You do not have enough money in your account to complete this transaction.")
        else:
            await context.respond(f"The user you're trying to wire funds to doesn't seem to exist or hasn't participated"
                                  f"in Shrimpy's economy yet. Have them register using /economy register and try again.")

    @economy.command(name="paycheck", description="Collect your weekly paycheck, if one is available")
    async def paycheck(self, context):
        row = db.execute(f"SELECT * FROM users WHERE id=?", (context.author.id,)).fetchone()
        if row is not None:
            last_paycheck_date = datetime.strptime(str(row[2]), '%Y%m%d%H%M%S')
            last_paycheck_diff = (datetime.today() - last_paycheck_date).days

            if last_paycheck_diff >= 7:
                today = datetime.today().strftime("%Y%m%d%H%M%S")
                db.execute(f'UPDATE users SET last_paycheck = {today}, balance = {row[1] + 500} WHERE id = '
                           f'{context.author.id}')
                db.commit()
                await context.respond(f"Hello <@{context.author.id}>! Your paycheck of $500 has been dispensed.")
            else:
                await context.respond(f"Hello <@{context.author.id}>! You still have {7 - last_paycheck_diff} days "
                                      f"until your next paycheck.")
        else:
            await context.respond(f"Hello <@{context.author.id}>! In order to collect your paycheck, you must first "
                                  f"run '/economy register'.")
            # await context.respond(f"User {row[0]}, you have ${row[1]}, and you got your last paycheck on {row[2]}")

    @economy.command(name="register", description="Register for the Shrimpy Economy")
    async def register(self, context):
        row = db.execute(f"SELECT * FROM users WHERE id=?", (context.author.id,)).fetchone()
        today = datetime.today().strftime("%Y%m%d%H%M%S")
        if row is None:
            db.execute(f'INSERT INTO users (id, balance, last_paycheck) VALUES ({context.author.id}, {500}, {today})')
            db.commit()
            await context.respond(f"Congrats, you have been registered with the Shrimpy Economy. Your starting "
                                  f"balance is $500.")
        else:
            await context.respond(f"You have already registered with the Shrimpy Economy.")


def setup(bot):
    bot.add_cog(Economy(bot))
