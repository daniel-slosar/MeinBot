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
import textwrap
import qrcode
import shutil
from covid import Covid
from discord.ext import commands
from discord.utils import get
from discord.voice_client import VoiceClient
from discord import FFmpegPCMAudio
from async_timeout import timeout
from functools import partial
from itertools import cycle
from asyncio import sleep
import lyricsgenius
import math
import platform

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

token = open("D:\\Python\\MeinBot\\token.txt", "r").read()


def community_report(guild):
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

    return online, idle, offline

@client.command()
async def rules(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(file=discord.File('rules.gif'))
    embed = discord.Embed(title="RULES!",colour=0xff0000,url="https://daydream404.github.io/MeinBot/",description="READ THE RULES!\n\n**0000. Respect everyone.\n\n0001. Use channels properly.\n\n0010. Speak only English.\n\n0011. Do not spam.\n\n0100. Do not advertise.\n\n0101. Do not post anything NSFW or you'll get banned.\n\n0110. Do not swear or use abusive language.\n\n0111. Do not start conversation with controversial topics.\n\n1000. Do not mention @everyone.\n\n1001. Do not share any files for download.**\n\nAfter reading the rules confirm accepting them by reacting with :thumbsup:")
    await ctx.send(embed=embed)


@client.command()
@commands.has_role("FÜHRER")
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member} has been kicked")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        embed = discord.Embed(title="Kick Error", description=f"Missing Permission!",colour=0x520081)
        await ctx.send(embed=embed)


@client.command()
@commands.has_role("FÜHRER")
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member} has been kicked")

@kick.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        embed = discord.Embed(title="Ban Error", description=f"Missing Permission!",colour=0x520081)
        await ctx.send(embed=embed)


@client.event
async def on_voice_state_update(member, before, after):
    #(519894723352199198)
    if before.channel is None and after.channel is not None:
        if after.channel.id == 515158430751784960 and member.id == 472502168738463755:
            user = client.get_user(373934947091742721)
            await user.send(f"{member} just joined the Room 1!")
            
        elif after.channel.id == 713819586482405496 and member.id == 472502168738463755:
            user = client.get_user(373934947091742721)
            await user.send(f"{member} just joined the Room 2!")

        elif after.channel.id == 699342733487243291 and member.id == 472502168738463755:
            user = client.get_user(373934947091742721)
            await user.send(f"{member} just joined the Room 3!")
        
        else:
            pass

    elif after.channel is None and member.id == 472502168738463755:
        user = client.get_user(373934947091742721)
        await user.send(f"{member} just left the room!\n------------------------------------------------")
    
    else:
        pass


@client.command()
async def help(ctx):
	embed=discord.Embed(colour=0x520081,title="MeinBot Help",url="https://daydream404.github.io/MeinBot/", description=":tools:  Commands list [here](https://google.com)\n\n :interrobang:  Any questions? [FAQ](https://google.com)\n\n:desktop:  Join our Discord! [Discord server](https://google.com)")
	embed.set_thumbnail(url=client.user.avatar_url)
	await ctx.send(embed=embed)

@client.command()
async def avatar(ctx, member: discord.Member = None):
	member = ctx.author if not member else member
	embed=discord.Embed(colour=0x520081,title="AVATAR")
	embed.set_image(url=member.avatar_url)
	await ctx.send(embed=embed)

@client.command()	
async def info(ctx):
    pltf = platform.platform()
    embed = discord.Embed(colour=0x520081, title="INFO",timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(name="Name: ", value="MeinBot#1050")
    embed.add_field(name="Creation date: ", value="01 May 2019")
    embed.add_field(name="Created by: ", value="01001100#2651")
    embed.add_field(name="Running on: ", value=pltf)
    embed.add_field(name="Help command:", value=f"`.help`")
    await ctx.send(embed=embed)


@client.command()
async def pi(ctx):
    pi_num = '{:.{}f}'.format(math.pi, 31)
    embed = discord.Embed(colour=0x520081)
    embed.add_field(name="π number:", value=pi_num)
    await ctx.send(embed=embed)

@client.command()
async def e(ctx):
    e = '{:.{}f}'.format(math.e, 31)
    embed = discord.Embed(colour=0x520081)
    embed.add_field(name="e number:", value=e)
    await ctx.send(embed=embed)


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
        embed = discord.Embed(title="Error", description=f"What should I repeat? `.repeat Hello!`",colour=0x520081)
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
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount + 1)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title="Error", description=f"You need to specify a number of messages to be deleted! `.clear 5`",colour=0x520081)
        await ctx.send(embed=embed)


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
        embed = discord.Embed(title="Error", description=f"You need to specify number as days `.days 356`",colour=0x520081)
        await ctx.send(embed=embed)


@client.command()
async def corona(ctx, krajina):
    global meinbot_guild
    try:
        covid = Covid(source="worldometers")
        cases_corona = covid.get_status_by_country_name(krajina)
        country = cases_corona['country']
        confirmed = cases_corona['confirmed']
        new_cases = cases_corona['new_cases']
        deaths = cases_corona['deaths']
        recovered = cases_corona['recovered']
        active = cases_corona['active']
        critical = cases_corona['critical']
        new_deaths = cases_corona['new_deaths']
        total_tests = cases_corona['total_tests']

        embed = discord.Embed(title="COVID-19", colour=0x520081, timestamp=ctx.message.created_at)
        embed.set_thumbnail(url="https://d2v9ipibika81v.cloudfront.net/uploads/sites/193/covid19-cdc-unsplash-2.jpg") 
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Country: ", value=country)
        embed.add_field(name="Confirmed: ", value=confirmed)
        embed.add_field(name="Recovered: ", value=recovered)
        embed.add_field(name="Active: ", value=active)
        embed.add_field(name="Deaths: ", value=deaths)
        embed.add_field(name="New Cases: ", value=f'+{new_cases}')
        embed.add_field(name="New Deaths: ", value=f'+{new_deaths}')
        embed.add_field(name="Critical: ", value=critical)
        embed.add_field(name="Total tests: ", value=total_tests)
        embed.add_field(name="Info: ", value="https://www.worldometers.info/coronavirus/")
        await ctx.channel.send(embed=embed)
    except:
        await ctx.channel.send(f"Cannot find this country, maybe try `.corona \"Dominican Republic\"` or try using `.countries`")

@corona.error
async def corona_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title="Error", description=f"You need to specify a country `.corona USA`",colour=0x520081)
        await ctx.send(embed=embed)


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
        embed = discord.Embed(title="Error", description=f"You need to specify text to be converted to QR CODE `.qr youtube.com`",colour=0x520081)
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
async def members(message):
    global meinbot_guild
    meinbot_guild = client.get_guild(515156152066244635)
    online, idle, offline = community_report(meinbot_guild)
    embed = discord.Embed(colour=0x520081,title="Members",description=f":green_circle: Online: {online} \n\n :red_circle: Busy/Idle: {idle} \n\n :white_circle:  Offline: {offline} \n\n :8ball: Server Count: {meinbot_guild.member_count} ")
    await message.channel.send(embed=embed)


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
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            pltf = platform.platform()
            member = client.get_user(573091512066375690)
            await channel.send("Hi, my name is MeinBot. I\'m your new bot!")
            embed = discord.Embed(colour=0x520081, title="INFO")
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="Name: ", value="MeinBot#1050")
            embed.add_field(name="Creation date: ", value="01 May 2019")
            embed.add_field(name="Created by: ", value="01001100#2651")
            embed.add_field(name="Running on: ", value=pltf)
            embed.add_field(name="Help command: ", value=f"`.command`")
            await channel.send(embed=embed)
            break


@client.event
async def on_member_join(member):
    if meinbot_guild == client.get_guild(515156152066244635):
        role = get(member.guild.roles, name="Peasant")
        await member.add_roles(role)
    else:
        pass

    for channel in member.text_channels:
        if channel.permissions_for(member.me).send_messages:
            #channel = client.get_channel(id=747512532930920588)
            embed = discord.Embed(colour=0x520081, description=f"Welcome to the party!")
            embed.set_thumbnail(url=f"{member.avatar_url}")
            embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
            embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
            embed.add_field(name=f"Your role: ", value=role)
            embed.timestamp = datetime.datetime.utcnow()
            await channel.send(embed=embed)
    

@client.command()
async def command(ctx):
    embed = discord.Embed(colour=0x520081, title="Meinbot", description="Commands:")
    embed.add_field(name=".members", value="Shows how many members are on the server")
    embed.add_field(name=".status", value="Shows online/offline/idle status")
    embed.add_field(name=".userinfo", value="Shows info about user (.userinfo @user)")
    embed.add_field(name=".clear", value="Delete certain amount of messages (.clear 5)")
    embed.add_field(name=".q", value="Ask your troubling questions and bot will reply")
    embed.add_field(name=".quote", value="Gives you a random quote")
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



    if "pornhub" in message.content.lower():
        await message.channel.send("Rate this porn you watched! I\'ll give it..")
        random_emojis = ('0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟','💯','👌🏾')
        time.sleep(2)
        emoji = random.choice(random_emojis)
        await message.add_reaction(emoji)

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) in ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟', '💯','👌🏾']
        
        try:
        	reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
        except asyncio.TimeoutError:
            await message.channel.purge(limit=1)
        else:
            await message.channel.purge(limit=1)


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


#loading cogs
extensions = ['googlestuff','social']
for ext in extensions:
    client.load_extension(ext)

client.run(token)

