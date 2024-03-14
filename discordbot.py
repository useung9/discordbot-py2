from cmath import log
import discord
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = 'MTE4OTgxNjQ5NTA0ODQ5OTI1MA.GDUHsV.r-3AZa4fS63VSuc5he9lbIv6hvXioeXAogwZtc'
GUILD_ID = '656116379967291393'  # 특정 서버의 ID

# 사용자 정보 ID (마스터)
masterUser ='396881467164196886'

# 관리 채널 (봇 사용자 등록 현황로그) : 1213831753450659880
manage_code = '1213831753450659880'


intents = discord.Intents.default()
intents.message = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'call':
        await message.channel.send("callback!")

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")