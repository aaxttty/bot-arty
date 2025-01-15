import os
import discord
from discord.ext import commands

from myserver import server_on

bot = commands.Bot(command_prefix='a.', intents=discord.Intents.all())



# bot พร้อมใช้งาน
@bot.event
async def on_ready():
    print("Bot ready!")

# คนเข้าเซิฟ
@bot.event
async def on_member_join(member):
    channel = bot.get_channel() #ID ห้อง
    text = f"Welcome to the server, {member.memtion}!"
    await member.send(text) #ส่งข้อความส่วนตัว

# คนออกเซิฟ
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel() #ID ห้อง
    text = f"Thank you,{member.memtion}!"
    await member.send(text)

# ส่งข้อความ
@bot.event
async def on_message(message):
    mes = message.content
    if mes == 'hello':
        await message.channel.send("ควย")

    elif mes == 'hi bot':
        await message.channel.send("Hello, " + str(message.author.name))

    await bot.process_commands(message)

# คำสั่งบอท
@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx. author.name}!")

server_on()

bot.run(os.getenv('TOKEN'))