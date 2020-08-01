# id 573091512066375690
# token NTczMDkxNTEyMDY2Mzc1Njkw.XMlzkQ.R2OTwor5q8bHLWK1cf6B_t2zucw
# 522304
# https://discordapp.com/oauth2/authorize?client_id=573091512066375690&scope=bot&permissions=522304
import asyncio  
import time
import discord
import traceback
import itertools
import random
from discord.ext import commands, tasks
from discord.utils import get
from discord.voice_client import VoiceClient
from discord import FFmpegPCMAudio
from functools import partial
from asyncio import sleep
from covid import Covid

client = commands.Bot(command_prefix = '.')


def community_report(guild):
    online = 0
    idle = 0
    offline = 0

    for m in guild.members:
        if str(m.status) == "online":
            online += 1
        if str(m.status) == "offline":
            offline += 1
        else:
            idle += 1

    return online, idle, offline


@client.event  # event decorator/wrapper
async def on_ready():
    global meinbot_guild
    meinbot_guild = client.get_guild(515156152066244635)
    print(f"We have logged in as {client.user}")


@client.command()
async def corona(message):
    global meinbot_guild
    covid = Covid()
    countries = covid.list_countries()
    krajina = input()
    cases_corona = covid.get_status_by_country_name(krajina)
    print(cases_corona)


@client.event
async def on_message(message):
    global meinbot_guild
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if "members" == message.content.lower():
        await message.channel.send(f"```\n{meinbot_guild.member_count}```")

    elif "logout" == message.content.lower():
        await client.close()

    elif "community" == message.content.lower():
        online, idle, offline = community_report(meinbot_guild)
        await message.channel.send(f"```Online: {online}.\nIdle/busy/dnd: {idle}.\nOffline: {offline}```")




client.run("NTczMDkxNTEyMDY2Mzc1Njkw.XQTvlg.XeqEfzYeNYsct9wH0HYvE7KPLbs")


'''
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("We are here.")


@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    meinbot_guild = client.get_guild(515156152066244635)

    if "members" == message.content.lower():
        await message.channel.send(f"```Members: {meinbot_guild.member_count}```")

    elif ".logout" == message.content.lower():
        await client.close()

    elif "report" == message.content.lower():
        online = 0
        idle = 0
        offline = 0

        for m in meinbot_guild.members:
            if str(m.status) == "online":
                online += 1
            if str(m.status) == "offline":
                offline += 1
            else:
                idle += 1

        await message.channel.send(f"```Online: {online}\nIdle/Busy/DnD: {idle}\nOffline: {offline}```")


client.run("NTczMDkxNTEyMDY2Mzc1Njkw.XQTvlg.XeqEfzYeNYsct9wH0HYvE7KPLbs")
'''





















'''
@client.command()
async def status(ctx):
    online = 0
    idle = 0
    offline = 0

    for m in guild.members:
        if str(m.status) == "online":
            online += 1
        elif str(m.status) == "offline":
            offline += 1
        else:
            idle += 1

    await message.channel.send(f"```Online: {online}\n Offline: {offline}\n Idle: {idle}```")

@client.command()
async def members(ctx):
    await message.channel.send(f"```There are {client.get_guild(515156152066244635).member_count} members on this server```")


@client.event #event decorator/wrapper
async def on_ready():
    global meinbot_guild
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("something unimportant"))
    print(f"You've logged in as disc: {client.user}")
    for member in client.get_all_members():
        print(member, member.status)



    bad_words = ["fuck", "pussy", "kid", "kokot", "debil", "retard"]
    await client.process_commands(message) 
    global meinbot_guild
    meinbot_guild =client.get_guild(573091512066375690)
    print(f"#{message.channel}: user {message.author}: {message.content}")

    elif ".status" in message.content.lower():
        online, idle, offline = community_report(client.get_guild(515156152066244635))
        await message.channel.send(f"```Online: {online}\n Offline: {offline}\n Idle: {idle}```")
        '''


