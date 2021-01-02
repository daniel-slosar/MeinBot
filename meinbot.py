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


intents = discord.Intents.all()

client = commands.Bot(command_prefix = '.', intents=intents)
client.remove_command('help')

global ROLE

token = open("D:\\Python\\MeinBot\\token.txt", "r").read() #windows
#token = open("/home/ec2-user/token.txt").read() linux


@client.command()
async def rules(ctx):
    embed = discord.Embed(title="RULES!",colour=0xff0000,url="https://daydream404.github.io/MeinBot/",description="READ THE RULES!\n\n**0000. Respect everyone.\n\n0001. Use channels properly.\n\n0010. Speak only English.\n\n0011. Do not spam.\n\n0100. Do not advertise.\n\n0101. Do not post anything NSFW or you'll get banned.\n\n0110. Do not swear or use abusive language.\n\n0111. Do not start conversation with controversial topics.\n\n1000. Do not mention @everyone.\n\n1001. Do not share any files for download.**\n\nAfter reading the rules confirm accepting them by reacting with :thumbsup:")
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
	embed=discord.Embed(colour=0x520081,title="MeinBot Help",url="https://daydream404.github.io/MeinBot/", description=":tools:  Commands list [here](https://google.com)\n\n :interrobang:  Any questions? [FAQ](https://google.com)\n\n:desktop:  Join our Discord! [Discord server](https://google.com)")
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
        embed = discord.Embed(title="Error", description=f"You need to specify question `.q Am I gay?`",colour=0x520081)
        await ctx.send(embed=embed)


@client.command()
async def clear(ctx, amount : int=1):
    await ctx.channel.purge(limit=amount + 1)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title="Error", description=f"You need to specify a number of messages to be deleted! `.clear 5`",colour=0x520081)
        await ctx.send(embed=embed)


@client.command()
async def rn(ctx,s: int = 1 , e: int = 99):
    r = random.randint(s,e)
    await ctx.send(f"```css\nRandom Number: {r}```")


@client.command()
async def yn(ctx, n: int=1):
    choices = ['Yes', 'No']
    for i in range(n):
        await ctx.send(f"```css\n{random.choice(choices)}```")


@client.command()
async def countries(message):
    global meinbot_guild
    await message.channel.send("Here\'s the link for all countries: " + "https://github.com/Daydream404/meinbot/blob/master/countries.txt")


@client.command()#needable
async def role(ctx, role):
    global server_id
    server_id = ctx.message.guild.id
    print(server_id)
    global ROLE
    ROLE = role
    print(ROLE)
    

@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Command Error", description=f"Command does not exist! Try `.help`",colour=0x520081)
        await ctx.send(embed=embed)


@client.event #event decorator/wrapper
async def on_ready():
    global meinbot_guild
    print(f"You've logged in as: {client.user}")
    await client.change_presence(activity=discord.Game("with your sister"))


@client.event
async def on_member_join(member):
    server_id = member.guild.id
    if server_id == 515156152066244635:
        print("GermanReich")
        channel = client.get_channel(768940272561946645)
        await channel.edit(name = '📊Member count: {}'.format(channel.guild.member_count))

        #channel = client.get_channel(769528310552068106)
        print(member)
        embed = discord.Embed(title="RULES!",colour=0xff0000,url="https://daydream404.github.io/MeinBot/",description="READ THE RULES!\n\n**0000. Respect everyone.\n\n0001. Use channels properly.\n\n0010. Speak only English.\n\n0011. Do not spam.\n\n0100. Do not advertise.\n\n0101. Do not post anything NSFW or you'll get banned.\n\n0110. Do not swear or use abusive language.\n\n0111. Do not start conversation with controversial topics.\n\n1000. Do not mention @everyone.\n\n1001. Do not share any files for download.**\n\nAfter reading the rules confirm accepting them by reacting with :thumbsup:")
        #await channel.send(embed=embed)
        await member.send(embed=embed)

            
        def check(reaction, user):
            return user == member and str(reaction.emoji) in ['👍']
        
        reaction, user = await client.wait_for("reaction_add", check=check)
        
        role = get(member.guild.roles, name="Landwirt")
        await member.add_roles(role)

        meinbot_guild = client.get_guild(515156152066244635)
        #meinbot_guild je GermanReich
        #server_id je 515156152066244635
        for channel in meinbot_guild.text_channels:
            if channel.permissions_for(meinbot_guild.me).send_messages:
                embed = discord.Embed(colour=0x520081, description=f"Welcome to the party!")
                embed.set_thumbnail(url=f"{member.avatar_url}")
                embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
                embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
                embed.add_field(name=f"Your role: ", value=role)
                embed.timestamp = datetime.datetime.utcnow()
                await channel.send(embed=embed)
                break

    elif server_id == 751897980432547941:
        print("MeinbotServer")
        channel = client.get_channel(768941337927352342)
        await channel.edit(name = '📊Member count: {}'.format(channel.guild.member_count))
        role = get(member.guild.roles, name="noob")
        await member.add_roles(role)

        meinbot_guild = client.get_guild(751897980432547941)
        for channel in meinbot_guild.text_channels:
            if channel.permissions_for(meinbot_guild.me).send_messages:
                embed = discord.Embed(colour=0x520081, description=f"Welcome to the party!")
                embed.set_thumbnail(url=f"{member.avatar_url}")
                embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
                embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
                embed.add_field(name=f"Your role: ", value=role)
                embed.timestamp = datetime.datetime.utcnow()
                await channel.send(embed=embed)
                break

    else:
        try:
            role = get(member.guild.roles, name=ROLE)
            await member.add_roles(role)
        except Exception as e:
            #await channel.send(e)
            await channel.send("Well you fucked up something didn\'t you? Try Help on my [website](https://www.meinbot.com)")   


@client.event
async def on_member_update(before, after):
    if before.raw_status == "offline" and after.raw_status == "online" and int(before.id) == 472502168738463755:
            user = client.get_user(373934947091742721)
            await user.send(f"{member} is Online!")
    

@client.event
async def on_member_remove(member):
    server_id = member.guild.id
    if server_id == 515156152066244635:
        channel = client.get_channel(768940272561946645)
        await channel.edit(name = '📊Member count: {}'.format(channel.guild.member_count))

        meinbot_guild = client.get_guild(server_id)
        for channel in meinbot_guild.text_channels:
            if channel.permissions_for(meinbot_guild.me).send_messages:
                embed = discord.Embed(colour=0x520081, description=f"Left the party!")
                embed.set_thumbnail(url=f"{member.avatar_url}")
                embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
                embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
                embed.add_field(name=f"We won\'t miss you..", value="Don\'t worry!")
                embed.timestamp = datetime.datetime.utcnow()
                await channel.send(embed=embed)
                break
    
    elif server_id == 751897980432547941:
        channel = client.get_channel(768941337927352342)
        await channel.edit(name = '📊Member count: {}'.format(channel.guild.member_count))
        
        meinbot_guild = client.get_guild(server_id)
        for channel in meinbot_guild.text_channels:
            if channel.permissions_for(meinbot_guild.me).send_messages:
                embed = discord.Embed(colour=0x520081, description=f"Left the party!")
                embed.set_thumbnail(url=f"{member.avatar_url}")
                embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
                embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
                embed.add_field(name=f"We won\'t miss you..", value="Don\'t worry!")
                embed.timestamp = datetime.datetime.utcnow()
                await channel.send(embed=embed)
                break

    else:
        pass



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



@client.event 
async def on_message(message):  # event that happens per any message.
    bad_words = ["oliver ma maly pipik", "daniel ma maly pipik"]
    await client.process_commands(message) 
    global meinbot_guild
    print(f"#{message.channel}: user {message.author}: {message.content}")

    '''if "pornhub" in message.content.lower():
        random_emojis = ('0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟','💯','👌🏾')
        time.sleep(2)
        emoji = random.choice(random_emojis)
        await message.add_reaction(emoji)'''



@client.command()
async def exit(ctx):
    #await ctx.send("Shutting down...")
    await client.close()


#loading cogs
extensions = ['googlestuff','social','basic','modules']
for ext in extensions:
    client.load_extension(ext)

client.run(token)



