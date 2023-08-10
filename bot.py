import discord 
from discord.ext import commands 
bot = commands.Bot(command_prefix = ">", intents = discord.Intents.all())

@bot.command(aliases = ['пинг'])
async def ping(ctx):
	await ctx.send("pong!")

@bot.event
async def on_ready():
	print("I am connected!")

@bot.event
async def on_message_edit(before, after):
	if before.content == after.content:
		return
	await before.channel.send(f"Message changed!\n{before.content} -> {after.content}")

bot.run("ODgyMjEwNjUyMDQxNjc0Nzky.YS4Esg.bWrL1GGJetS5xU0egZCgHI0CQt0")
