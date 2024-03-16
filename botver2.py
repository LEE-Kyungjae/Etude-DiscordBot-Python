import youtube_dl
import os
import asyncio
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

client = discord.Client(intents=discord.Intents.default())
token = os.getenv("TOKEN")
bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
embed = discord.Embed(title="Embed title", description="Embed description", color=0x36ccf2)

@bot.event
async def on_ready():
    print("Logged in as ")
    print(bot.user.id)
    print(bot.user.name)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("죄수들과 술래잡기"))
    print("준비완료")
    

@bot.command(aliases=['하이', 'ㅎㅇ', 'hi', 'nig', 'bro'])
async def 안녕(ctx):
    await ctx.send(f'입니다.')    

@bot.command(name="울어")
async def cry(ctx):
    await ctx.send(f'ㅠㅠ')    

@bot.command()
async def dice(ctx):
    randnum = random.randint(1, 6)  # 1이상 6이하 랜덤 숫자를 뽑음
    await ctx.send(f'주사위 결과는 {randnum} 입니다.')    
    
@bot.command()
async def mine(ctx):
    minerals = ['다이아몬드', '루비', '에메랄드', '자수정', '철', '석탄']
    weights = [1, 3, 6, 15, 25, 50]
    results = random.choices(minerals, weights=weights, k=5)  # 광물 5개를 가중치에 따라 뽑음
    await ctx.send(', '.join(results) + ' 광물들을 획득하였습니다.')

@bot.command()
async def emb(ctx):
    embed = discord.Embed(title="결과",description='description', url='https://howbeautifulworld.tistory.com/', color=discord.Color.green())
    embed.add_field(name='field 1 title', value='field 1 value', inline=True)
    embed.add_field(name='field 2 title', value='field 2 value', inline=True)
    embed.add_field(name='field 3 title', value='field 3 value', inline=True)
    embed.add_field(name='field 4 title', value='field 4 value', inline=True)
    #avatar_url="https://cdn.discordapp.com/avatars/234979767818911744/096e9209832a7919ad6faf8627188e93.png"
    #embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=ctx.author.display_name)
    await ctx.send(embed=embed)

bot.run(token)