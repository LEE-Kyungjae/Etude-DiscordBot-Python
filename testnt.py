import youtube_dl
import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

token = os.getenv("TOKEN")
#bot = commands.Bot(command_prefix='!')  # 봇의 접두사 설정
bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

@bot.event
async def on_ready():  # 봇 준비 시 1회 동작하는 부분
    # 봇 이름 하단에 나오는 상태 메시지 및 상태 설정
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("반갑습니다 :D"))
    print("Bot is ready")


@bot.command()  # 봇 명령어
async def hello(ctx):  # !hello라고 사용자가 입력하면
    await ctx.send("Hello world")  # 봇이 Hello world라고 대답함

bot.run(token)