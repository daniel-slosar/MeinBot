import asyncio  
import time
import datetime
import discord
import os
import sys
import traceback
import itertools
import random
#import imdb
import json
import textwrap
import qrcode
import shutil
#from covid import Covid
from discord.ext import commands
from discord.utils import get
from discord.voice_client import VoiceClient
from discord import FFmpegPCMAudio
from discord import Member as member
from async_timeout import timeout
from functools import partial
from itertools import cycle
from asyncio import sleep
#import lyricsgenius
import math
from urllib.request import urlopen
import requests

intents = discord.Intents.all()

client = commands.Bot(command_prefix = '.', intents=intents)
client.remove_command('help')


token = open("D:\\Python\\MeinBot\\token.txt", "r").read() #windows
#token = open("/home/ec2-user/token.txt").read() #linux

names = ["011001100", "Pipikator25", "Themm"]

@client.command()
async def commandslist(ctx):
    embed = discord.Embed(title="Commands list",colour=0xff0000,url="https://daydream404.github.io/MeinBot/",description="`.info` Returns basic info about bot\n\n`.userinfo @user` Returns basic info about user\n\n`.repeat LOL` Repeats the message \n\n`.poke @user 5` Mentions the @user n-times with delay\n\n`.rand 1 25` RND! You can specify interval <x,y>\n\n`.yn` Yes or No\n\n `.help` Help command\n\n")
    await ctx.send(embed=embed)


@client.command()
async def rules(ctx):
    embed = discord.Embed(title="RULES!",colour=0xff0000,url="https://daydream404.github.io/MeinBot/",description="READ THE RULES!\n\n**0000. Respect everyone.\n\n0001. Use channels properly.\n\n0010. Speak only English.\n\n0011. Do not spam.\n\n0100. Do not advertise.\n\n0101. Do not post anything NSFW or you'll get banned.\n\n0110. Do not swear or use abusive language.\n\n0111. Do not start conversation with controversial topics.\n\n1000. Do not mention @everyone.\n\n1001. Do not share any files for download.**\n\nAfter reading the rules confirm accepting them by reacting with :thumbsup:")
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
	embed=discord.Embed(colour=0x520081,title="MeinBot Help",url="https://daydream404.github.io/MeinBot/", description=":tools:  Commands list [here](https://daydream404.github.io/MeinBot/)\n\n :interrobang:  Any questions? [FAQ](https://daydream404.github.io/MeinBot/)\n\n:desktop:  Join our Discord! [Discord server](https://discord.gg/PjYewPngVe)")
	embed.set_thumbnail(url=client.user.avatar_url)
	await ctx.send(embed=embed)


@client.command()
async def q(ctx, *, question):
    responses = ['It is certain.',
                 'Without a doubt',
                 'Yes', 'Affirmative!',
                 'Negative!', 'Most likely',
                 'Very doubtful', 'Yes, but you\'re still faggot',
                 'No', 'Ask again later',
                 'Cannot predict now', 'Maybe', 'How tf should I know?']
    embed = discord.Embed(colour=0x520081)
    embed.set_thumbnail(url="https://i.kym-cdn.com/photos/images/facebook/001/151/543/119.jpg")
    embed.set_author(name="Questionnaire")
    embed.add_field(name="Question:", value=question,inline=False)
    embed.add_field(name="Answer:", value=random.choice(responses), inline=True)
    await ctx.send(embed=embed)

@q.error
async def q_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title="Error", description=f"You need to specify question `.q Should I go outside?`",colour=0x520081)
        await ctx.send(embed=embed)


@client.command()
async def clear(ctx, amount : int=1):
    amount = amount + 1
    for i in range(amount):
        await ctx.channel.purge(limit=1)
        time.sleep(0.8)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title="Error", description=f"You need to specify a number of messages to be deleted! `.clear 5`",colour=0x520081)
        await ctx.send(embed=embed)


@client.command()
async def countries(message):
    global meinbot_guild
    await message.channel.send("Here\'s the link for all countries: " + "https://github.com/Daydream404/meinbot/blob/master/countries.txt")
    

@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        x = str(error)
        x = x.split()[1]
        if x == '"BMI"':
            pass
        else:
            embed = discord.Embed(title="Command Error", description=f"Command does not exist! Try `.commandslist` or `.help`",colour=0x520081)
            await ctx.send(embed=embed)


@client.event #event decorator/wrapper
async def on_ready():
    global meinbot_guild
    print(f"You've logged in as: {client.user}")
    await client.change_presence(activity=discord.Game("with your sister"))


@client.command()
async def command(ctx):
    embed = discord.Embed(colour=0x520081, title="Meinbot", description="Commands:")
    embed.add_field(name=".userinfo", value="Shows info about user (.userinfo @user)")
    embed.add_field(name=".clear", value="Delete certain amount of messages (.clear 5)")
    embed.add_field(name=".q", value="Ask your troubling questions and bot will reply")
    embed.add_field(name=".corona", value="Gives you corona update(.corona US/Slovakia/Czechia)")
    embed.add_field(name=".countries", value="Gives you link to all countries")
    embed.add_field(name=".translate", value="Translator from detected language to english (.translate Okno)")
    embed.add_field(name=".google", value="Googles for you, shows you first 3 searches on google (.google cafe Paris)")
    embed.add_field(name=".wiki", value="Wiki any site page you want! (.wiki Hitler)")
    embed.add_field(name=".rn", value="Random number generator (.rn) or (.rn 1 99)-from 1 to 99")
    embed.add_field(name=".movie", value="Gives you random movie from IMDb TOP 250 Movies database (.movie)" )
    await ctx.send(embed=embed)


@client.command()
async def rl(ctx):
    random_list = random.choice(names)
    embed=discord.Embed(colour=0x520081,title="Rocket League Tournament", description=f"List: `{names}`\n__ __Random Choice: __**{random_list}**__")
    embed.set_thumbnail(url="https://rocketleague.media.zestyio.com/rl_s2_core_1920x1080_no-logos.jpg")
    await ctx.send(embed=embed)


@client.command()
async def addrl(ctx,new):
    names.append(new)
    await ctx.send(f"{new} was added to the list!")
    

@client.event 
async def on_message(message):  # event that happens per any message.
    bad_words = ["oliver ma maly pipik", "daniel ma maly pipik"]
    await client.process_commands(message) 
    global meinbot_guild
    print(f"#{message.channel}: user {message.author}: {message.content}")

    if message.content.startswith('.BMI'): #.BMI
        channel = message.channel
        await channel.send("What\'s your height?")
        def height_func(m):
            return " cm" in m.content and m.channel == channel

        msg = await client.wait_for('message', check=height_func)
        msg = msg.content
        height= float(msg[0] + msg[1] + msg[2])
        height = height /100
        print(height)

        await channel.send("What\'s your weight?")
        def weight_func(m):
            return " kg" in m.content and m.channel == channel

        msg = await client.wait_for('message', check=weight_func)
        msg = msg.content
        weight= float(msg[0] + msg[1] + msg[2])
        print(weight)
        bmi = weight/pow(height,2)
        if bmi >= 25.0 and bmi <= 29.9:
            embed = discord.Embed(title="Body Mass Index", description=f"**You are Overweight!**",colour=0xffea00)
            embed.set_thumbnail(url="https://www-assets.withings.com/pages/health-insights/about-body-mass-index/media/bmi-chart.png")
            await channel.send(embed=embed)
        elif bmi >= 18.5 and bmi <= 24.9:
            embed = discord.Embed(title="Body Mass Index", description=f"**You have a Normal Weight!**",colour=0x00ff04)
            embed.set_thumbnail(url="https://www-assets.withings.com/pages/health-insights/about-body-mass-index/media/bmi-chart.png")
            await channel.send(embed=embed)
        elif bmi < 18.5:
            embed = discord.Embed(title="Body Mass Index", description=f"**You are Underweight!**",colour=0x00bbff)
            embed.set_thumbnail(url="https://www-assets.withings.com/pages/health-insights/about-body-mass-index/media/bmi-chart.png")
            await channel.send(embed=embed)
        elif bmi >= 30.0 and bmi <=34.9:
            embed = discord.Embed(title="Body Mass Index", description=f"**You are Obese!**",colour=0xff8800)
            embed.set_thumbnail(url="https://www-assets.withings.com/pages/health-insights/about-body-mass-index/media/bmi-chart.png")
            await channel.send(embed=embed)
        elif bmi>=35:
            embed = discord.Embed(title="Body Mass Index", description=f"**You are Extremely Obese!**",colour=0xff0000)
            embed.set_thumbnail(url="https://www-assets.withings.com/pages/health-insights/about-body-mass-index/media/bmi-chart.png")
            await channel.send(embed=embed)
        else:
            await channel.send("Something is not right")

@client.command()
async def exit(ctx):
    await ctx.channel.purge(limit=1)    
    await client.close()


#loading cogs
extensions = ['googlestuff','social','basic','modules','members']
for ext in extensions:
    client.load_extension(ext)

client.run(token)



