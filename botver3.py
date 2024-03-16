import discord 
import asyncio
import os
import random
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()


#토큰


#인텐트 설정
#디스코드의 기본 설정을 따른다.
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".",intents=intents)


#시작
@bot.event
async def on_ready():
    print("user id : " + str(bot.user.id))
    print("user name : " + str(bot.user.name))
    print(f'{bot.user}로 로그인하였습니다!')
    await bot.tree.sync(guild=discord.Object(id=1175316249941651557))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("죄수들과 술래잡기"))
    print("부팅이 완료되었습니다.")


@bot.tree.command(
    name="blep")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("blep command repeated")
    print("blep 커멘드 사용됨")
    
@bot.tree.command(
    name="blep2")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("blep command repeated")
    print("blep2 커멘드 사용됨")


    
    
    
@bot.tree.command(
    name="test",
    description="test slash command")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("test slash command repeated")
    print("test 커멘드 사용됨")



@bot.tree.command(
    name="mannu",
    description="Mannu is a good boy")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("Hello World!")
    print("mannu 커멘드 사용됨")
    
@bot.tree.command(
    name="173",
    description="now 173 watch you")
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message("test slash command repeated")
    print("test 커멘드 사용됨")

# @bot.tree.command(name="test",description="test command")
# async def slash_command(interaction:discord.Integration):
#     await interaction.response.send_message("test command repeat")

@bot.event
async def on_message_edit(before,after):
        print("asd")
        #await message.channel.send("input")


# @bot.command()
# async def hello(ctx):
#     await ctx.send("Hii There! I am Mannu And Welcome to the discord.py tutorial")    

@bot.command
async def hello(ctx):
    ctx.send("제대로 작동하지않음")



#메시지 읽어서 반응시키기
@bot.event
async def on_message(message):
    if message.content == "응답":
        await message.channel.send("{}|{}, 님 안녕하세요!".format(message.author,message.author.mention))
    # 사용자한테 입력받은 디엠 메시지를 사용자의 개인메시지로 보내준다
    if message.content.startswith("!dm"):
        output = str(message.content.split(" ")[1])
        embed = discord.Embed(title=message.author,description=output,color=0x36ccf2)
        await message.author.send(embed=embed)
        #await message.author.send("{}|{}, User, Hello".format(message.author,message.author.mention))
        #await message.author.send("{} 의 개인메시지: \"{}\"".format(message.author.mention,output))
        
    if message.content == "야":
        await message.channel.send("{}새끼 왜불러".format(message.author.mention))
    # 임베드 삽입(인용같은 글들 나오게하는거)
    if message.content == "임베드":
        await message.channel.send("달라하면 줘야하나..")
        embed = discord.Embed(title=str(bot.user.name),description=str(bot.user.verified),color=0x36ccf2)
        await message.channel.send(embed=embed)
    #임베드에 이미지 삽입
    if message.content == "이미지":
        embed = discord.Embed(title="제목",description="설명",color=0x36ccf2)
        embed.set_image(url="https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_92x30dp.png")
        await message.channel.send(embed=embed)
    #임베드에 썸네일과 푸터 달기
    if message.content == "썸넬푸터":
        embed = discord.Embed(title="제목",description="설명",color=0x36ccf2)
        embed.set_thumbnail(url="https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_92x30dp.png")
        embed.set_image(url="https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_92x30dp.png")
        embed.set_footer(text=message.author, icon_url=message.author.avatar.url)
        embed.add_field(name="필드제목", value="필드설명", inline=False)
        await message.channel.send(embed=embed)
    #메시지 삭제
    if message.content.startswith("!청소"):    
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메시지를 삭제했습니다.")
        
    

# 봇을 실행합니다.
bot.run(os.environ.get("TOKEN"))
        
