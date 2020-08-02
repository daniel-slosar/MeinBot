import asyncio  
import time
import datetime
import discord
import os
import sys
import traceback
import itertools
import random
import imdb
import json
import wikipedia
import textwrap
import qrcode
import shutil
from timeit import default_timer
from googletrans import Translator
from covid import Covid
from discord.ext import commands
from discord.utils import get
from discord.voice_client import VoiceClient
from discord import FFmpegPCMAudio
from async_timeout import timeout
from functools import partial
from itertools import cycle
from asyncio import sleep
from googlesearch import search
import instaloader

client = commands.Bot(command_prefix = '.')

token = open("D:\\Python\\MeinBot\\token.txt", "r").read()

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


@client.command()
async def ping(ctx):
    embed = discord.Embed(colour=0x520081, title="Ping")
    embed.add_field(name="Latency:", value=client.latency)
    await ctx.send(embed=embed)


@client.command()
async def repeat(ctx, *, msng):
    if msng == "I\'m stupid":
        await ctx.send("Yeah, we know..")
    elif msng == "I suck dicks":
        await ctx.send("Yes you do!")
    else:
        await ctx.send(msng)

@repeat.error
async def repeat_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(f"```css\nWTF should I repeat? (.repeat I\'m stupid)```")


@client.command()
async def ig(ctx, profile):
    profile1 = profile
    instg = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(instg.context, profile)
    instg.context.get_and_write_raw(profile.profile_pic_url, "instagram.jpg")
    await ctx.channel.send(f"<https://www.instagram.com/{profile1}/>")
    await ctx.channel.send(file=discord.File('instagram.jpg'))

@ig.error
async def ig_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(f"```css\nNeed some ig profile name (.ig selenagomez)```")


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
        await ctx.send(f"```css\nNeed some question mate.. (.q Am I sad?)```")


@client.command()
async def google(message,*, query):
    await message.channel.send("I'm searching google...")
    for i in search(query,lang='en',num=1,start=0,stop=1,pause=2):
        i1 = i
    for i in search(query,lang='en',num=1,start=0,stop=2,pause=2):
        i2 = i

    for i in search(query,lang="en",num=1,start=0,stop=3,pause=2):
        i3=i

    embed = discord.Embed(colour=0x520081)
    embed.set_thumbnail(url="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
    embed.set_author(name="Google Search")
    embed.add_field(name="1. Result", value=i1,inline=False)
    embed.add_field(name="2. Result", value=i2,inline=False)
    embed.add_field(name="3. Result", value=i3,inline=False)
    await message.channel.send(embed=embed)

@google.error
async def google_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(f"```css\nSearch on google with me! (.google Elon Musk)```")


@client.command(aliases=['w'])
async def wiki(ctx, *, question):
    try:
        a = wikipedia.summary(question)
        if len(a) <= 1023:
            embed = discord.Embed(colour=0x520081)
            embed.set_thumbnail(url="https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png")
            embed.add_field(name="Wikipedia", value = a)
            await ctx.send(embed=embed)

        elif 2048 > len(a) > 1024:
            a1, a2 = a[:len(a)//2],a[len(a)//2:]
            embed = discord.Embed(colour=0x520081)
            embed.set_thumbnail(url="https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png")
            embed.add_field(name="Wikipedia", value = a1)
            embed.add_field(name="** **", value = a2)
            await ctx.send(embed=embed)

        else: 
            a1 = textwrap.wrap(a, 1024)
            embed = discord.Embed(colour=0x520081)
            embed.set_thumbnail(url="https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png")
            embed.add_field(name="Wikipedia", value = a1[0])
            embed.add_field(name="** **", value = a1[1])
            embed.add_field(name="** **", value = a1[2])
            await ctx.send(embed=embed)
            
    except Exception as e:
        embed = discord.Embed(colour=0x520081)
        embed.set_thumbnail(url="https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png")
        embed.add_field(name="I didn\'t find anything like that try: ", value= e)
        await ctx.send(embed=embed)

@wiki.error
async def wiki_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(f"```css\nLearn on wiki with me! (.wiki Adolf Hitler)```")


@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount + 1)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(f"```css\nYou need to specify a number! (.clear 5)```")


@client.command()
async def chat(ctx):
	await ctx.author.send('Ooh..I heard you wanted to talk to me?')
	await ctx.author.send('So what\'s the problem?\nYou can still chill out on this site: https://www.pornhub.com')


@client.command()
async def days(ctx, days):
    now = datetime.datetime.now()
    thousandDays = datetime.timedelta(int(days))
    future_date = now + thousandDays
    final = future_date.strftime("%A %d/%m/%Y %H:%M:%S")
    days = future_date.strftime(days)
    final = future_date.strftime(final)
    embed = discord.Embed(colour=0x520081)
    embed.set_thumbnail(url="https://cdn.dribbble.com/users/2526497/screenshots/6175813/image.png")
    embed.add_field(name="** **", value=f"**{days}**" + " days from now will be " + f"**{final}**", inline=False)
    await ctx.send(embed=embed)

@days.error
async def days_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(f"```css\nYou need to specify a number! (.days 365)```")


@client.command()
async def corona(ctx, krajina, member: discord.Member = None):
    global meinbot_guild
    member = ctx.author if not member else member
    try:
        covid = Covid()
        #countries = covid.list_countries()
        cases_corona = covid.get_status_by_country_name(krajina)
        css_crn0 = json.dumps(cases_corona)
        country0 = css_crn0.split()[3]#italy
        country1 = country0.replace('",', '')
        country = country1.replace('"', '')
        confirmed0 = css_crn0.split()[5]#228006conf
        confirmed = confirmed0.replace(',', '')
        active0 = css_crn0.split()[7]#60960active
        active = active0.replace(',', '')
        deaths0 = css_crn0.split()[9]#32486deaths
        deaths = deaths0.replace(',', '')
        recovered0 = css_crn0.split()[11]#134recoverd
        recovered = recovered0.replace(',', '')

        embed = discord.Embed(title="COVID-19", colour=0x520081, timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://d2v9ipibika81v.cloudfront.net/uploads/sites/193/covid19-cdc-unsplash-2.jpg") 
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Country: ", value=country)
        embed.add_field(name="Confirmed: ", value=confirmed)
        embed.add_field(name="Active: ", value=active)
        embed.add_field(name="Deaths: ", value=deaths)
        embed.add_field(name="Recovered: ", value=recovered)
        embed.add_field(name="Info: ", value="https://www.who.int/")
        await ctx.channel.send(embed=embed)
    except:
        await ctx.channel.send("Cannot find this country.Try using .commands")

@corona.error
async def corona_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(f"```css\nYou need to specify a country! (.corona US)```")


@client.command()
async def movie(message):
    global meinbot_guild
    im = imdb.IMDb()
    search = im.get_top250_movies()
    i = random.randint(1,250)
    embed = discord.Embed(colour=0x520081)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/1200px-IMDB_Logo_2016.svg.png")
    embed.add_field(name="Movie you should watch: ", value=search[i], inline = True)
    embed.set_footer(text="https://www.imdb.com/") 
    await message.channel.send(embed=embed)
    

@client.command()
async def qr(ctx, *, data):
    qr = qrcode.QRCode(version=1,box_size=10,border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black",back_color="white")
    img.save("1.png")
    await ctx.channel.send(file=discord.File('1.png'))

@qr.error
async def qr_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(f"```css\nYou need to specify some text (.qr youtube.com)```")


@client.command(aliases=['t', 'tr', 'trns'])
async def translate(ctx, word: str, scnd_l: str="en"):
    translator= Translator()
    dtct = translator.detect(word)
    translated = translator.translate(word, src=dtct.lang, dest=scnd_l)
    embed = discord.Embed(colour=0x520081)
    embed.set_thumbnail(url="https://www.slashgear.com/wp-content/uploads/2019/12/google_translate_main-1280x720.jpg")
    embed.set_author(name="Translator")
    embed.add_field(name="From:", value=dtct.lang, inline=True)
    embed.add_field(name="To:", value=scnd_l, inline=True)
    embed.add_field(name="Confidence:", value=dtct.confidence, inline=True)
    embed.add_field(name="Orginal word:", value=word, inline=True)
    embed.add_field(name="Translated word:", value=translated.text, inline=True)
    await ctx.send(embed=embed)

@translate.error
async def translate_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(f"```css\nI need some word to translate (.translate okno)```")


@client.command()
async def rn(ctx,s: int = 1 , e: int = 99):
    r = random.randint(s,e)
    await ctx.send(f"```css\nRandom Number: {r}```")


@client.command()
async def yon(ctx, n: int=1):
    choices = ['Yes', 'No']
    for i in range(n):
        await ctx.send(f"```css\n{random.choice(choices)}```")


@client.command()
async def members(message):
    global meinbot_guild
    meinbot_guild = client.get_guild(515156152066244635)
    await message.channel.send(f"```py\nThere are {meinbot_guild.member_count} members on this server```")


@client.command()
async def status(message):
    global meinbot_guild
    meinbot_guild = client.get_guild(515156152066244635)
    online, idle, offline = community_report(meinbot_guild)
    await message.channel.send(f"```py\nMembers\nOnline: {online}\nIdle/Busy: {idle}\nOffline: {offline}```")


@client.command()
async def quote(message):
    quotesdic = ['\"Quiet people have the loudest minds\"- Steven Hawking',
                '\"While there is a life there is a hope\"- Steven Hawking',
                '\"Life is not fair. Get used to it.\"- Bill Gates',
                '\"Measuring programming progress by lines of code is like measuring aircraft building progress by weight.\"- Bill Gates',
                '\"Be nice to nerds. Chances are you’ll end up working for one.\"- Bill Gates',
                '\"We all need people who will give us feedback. That’s how we improve.\"- Bill Gates',
                '\"We are our choices. Build yourself a great story.\"- Jeff Bezos',
                '\"The beauty of me is that I\'m very rich.\"- Donald Trump',
                '\"When Mexico sends its people, they are not sending the best. They are bringing drugs, they are bringing crime. They are rapists and some, I assume, are good people\"- Donald Trump',
                '\"I think it is possible for ordinary people to choose to be extraordinary.\"- Elon Musk',
                '\"Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world\"- Albert Einstein',
                '\"The important thing is to not stop questioning. Curiosity has its own reason for existing\"- Albert Einstein',
                '\"The first step is to establish that something is possible; then probability will occur\"- Elon Musk',
                '\"I could either watch it happen or be a part of it\"- Elon Musk']
    await message.channel.send(f" {random.choice(quotesdic)}") 


@client.command()
async def countries(message):
    global meinbot_guild
    await message.channel.send("Here\'s the link for all countries: " + "https://github.com/Daydream404/meinbot/blob/master/countries.txt")


@client.command()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles] #roles= [] for roles in member.roles: roles.append(role) same shit
    
    embed = discord.Embed(colour=0x520081, timestamp=ctx.message.created_at)
    
    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Name:", value=member.display_name)
    
    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at server:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Bot", value=member.bot)

    await ctx.send(embed=embed)

'''
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        #await ctx.send(f"Well something went wrong! try `.commands`")
        await ctx.send("Well something went wrong! YOU fucked up..Again!")
'''

@client.event #event decorator/wrapper
async def on_ready():
    global meinbot_guild
    print(f"You've logged in as: {client.user}")
    await client.change_presence(activity=discord.Game("with your sister"))


@client.event
async def on_member_join(member):
    embed = discord.Embed(colour=0x520081, description=f"Welcome to the party!")
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()
    channel = client.get_channel(id=715866321966989312)
    await channel.send(embed=embed)


@client.command()
async def command(ctx):
    embed = discord.Embed(colour=0x520081, title="Meinbot", description="Commands:")
    embed.add_field(name=".members", value="Shows how many members are on the server")
    embed.add_field(name=".status", value="Shows online/offline/idle status")
    embed.add_field(name=".userinfo", value="Shows info about user (.userinfo @user)")
    embed.add_field(name=".chat", value="Starts chatting with you in private")
    embed.add_field(name=".clear", value="Delete certain amount of messages (.clear 5)")
    embed.add_field(name=".q", value="Ask your troubling questions and bot will reply")
    embed.add_field(name=".exit", value="Turn off the bot")
    embed.add_field(name=".quote", value="Gives you a random quote")
    embed.add_field(name=".time", value="Prints out time and date")
    embed.add_field(name=".corona", value="Gives you corona update(.corona US/Slovakia/Czechia)")
    embed.add_field(name=".countries", value="Gives you link to all countries")
    embed.add_field(name=".translate", value="Translator from detected language to english (.translate Okno)")
    embed.add_field(name=".google", value="Googles for you, shows you first 3 searches on google (.google cafe Paris)")
    embed.add_field(name=".wiki", value="Wiki any site page you want! (.wiki Hitler)")
    embed.add_field(name=".qr", value="Turns your message/link to qr code! (.qr https://google.com/)")
    embed.add_field(name=".rn", value="Random number generator (.rn) or (.rn 1 99)-from 1 to 99")
    embed.add_field(name=".movie", value="Gives you random movie from IMDb TOP 250 Movies database (.movie)" )
    await ctx.send(embed=embed)


@client.event 
async def on_message(message):  # event that happens per any message.
    bad_words = ["oliver ma maly pipik", "daniel ma maly pipik"]
    await client.process_commands(message) 
    global meinbot_guild
    print(f"#{message.channel}: user {message.author}: {message.content}")

    for word in bad_words:
        if message.content.count(word) > 0:
            await message.channel.purge(limit=1)
            await message.channel.send("Robo ma maly pipik\tRobo ma maly pipik\tRobo ma maly pipik\tRobo ma maly pipik\tRobo ma maly pipik\tRobo ma maly pipik\n" * 10)




    if "<@!724654875157201066>" in message.content.lower():
        emoji = '<:jarko:719935424696418446>'
        await message.add_reaction(emoji)


    if "<@!386529526479454223>" in message.content.lower():
        emoji = '<:pepesad:604586503250640896>'
        await  message.add_reaction(emoji)

    if "<@!472502168738463755>" in message.content.lower():
        emoji = '<:pepeamen:630159152689315850>'
        await  message.add_reaction(emoji)

    if "<@!373934947091742721>" in message.content.lower():
        emoji = '<:pepedrug:630161061420597289>'
        await  message.add_reaction(emoji)



@client.command()
async def exit(ctx):
    await ctx.send("Shutting down...")
    await client.close()


client.run(token)

