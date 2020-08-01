# id 573091512066375690
# token NTczMDkxNTEyMDY2Mzc1Njkw.XMlzkQ.R2OTwor5q8bHLWK1cf6B_t2zucw
# 522304
# https://discordapp.com/oauth2/authorize?client_id=573091512066375690&scope=bot&permissions=522304
import asyncio  
import time
import datetime
import discord
import os
import sys
import traceback
import itertools
import random
from discord.ext import commands, tasks
from discord.utils import get
from discord.voice_client import VoiceClient
from discord import FFmpegPCMAudio
from async_timeout import timeout
from functools import partial
from os import system
from itertools import cycle
from asyncio import sleep

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


@client.command(aliases=['_q'])
async def q(ctx, *, question):
    responses = ['It is certain.',
                 'Without a doubt',
                 'Yes', 'Affirmative!',
                 'Negative!', 'Most likely',
                 'Very doubtful']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Your Brain was Erased!")


@client.command()
async def chat(ctx):
	await ctx.author.send('Ooh..I heard you wanted to talk to me?')


@client.command()
async def members(ctx):
    meinbot_guild = client.get_guild(573093988832378900)
    await ctx.send(f"```Members are {meinbot_guild.member_count}```")


@client.command()
async def status(message):
    online, idle, offline = community_report(meinbot_guild)
    await message.channel.send(f"```py\nMembers:\nOnline: {online}.\nIdle/busy: {idle}.\nOffline: {offline}. \nWhoa, thats a lot of damage.```")


@client.command()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles] #roles= [] for roles in member.roles: roles.append(role) same shit
    
    embed = discord.Embed(colour=0xffd700, timestamp=ctx.message.created_at)
    
    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Guild name:", value=member.display_name)
    
    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at server:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Bot", value=member.bot)
    await ctx.send(embed=embed)


async def user_metrics_background_task():
    await client.wait_until_ready()
    global meinbot_guild


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('This command doesn\'t exist!')


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete.')


@client.event #event decorator/wrapper
async def on_ready():
    global meinbot_guild
    print(f"We have logged in as disc1: {client.user}")


@client.event
async def on_member_join(member):
    embed = discord.Embed(colour=0xffd700, description=f"Welcome to the party!")
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()

    channel = client.get_channel(id=582630805780824096)

    await channel.send(embed=embed)


@client.event 
async def on_message(message):  # event that happens per any message
    print(f"{message.channel}: {message.author}: {message.content}")
    global meinbot_guild
    meinbot_guild = client.get_guild(573093988832378900)

    if "-skip" in message.content.lower():
       await message.channel.send("Okay!")

    elif "robert" in message.content.lower():
        await message.channel.send("He\'s the one who talks to girls.")

    if "-play" in message.content.lower():
    	await message.channel.send("Working on it..")
   
    elif "stalin" in message.content.lower():
        await message.channel.send("Das bolschewistische Ungeheuer!")

    if "oliver" in message.content.lower():
        await message.channel.send("Wotko!")

    elif "daniel" in message.content.lower():
    	await message.channel.send("Creator!")

    if "members" in message.content.lower():
        await message.channel.send(f"```There are {meinbot_guild.member_count} members```")

    if "logout" in message.content.lower():
    	await client.close()

client.loop.create_task(user_metrics_background_task())
client.run("NTczMDkxNTEyMDY2Mzc1Njkw.XQTvlg.XeqEfzYeNYsct9wH0HYvE7KPLbs")

