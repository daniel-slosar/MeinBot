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
import lyricsgenius
import math
from google_currency import convert
import platform

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

token = open("D:\\Python\\MeinBot\\token.txt", "r").read()
token_genius = open(":\\Python\\MeinBot\\genius_token.txt", "r").read()


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
    member == client.get_user(519894723352199198)
    if before.channel is None and after.channel is not None:
        if after.channel.id == 515158430751784960 and member == client.get_user(519894723352199198):
            user = client.get_user(373934947091742721)
            await user.send(f"{member} just joined the Room 1!")
            
        elif after.channel.id == 713819586482405496 and member == client.get_user(519894723352199198):
            user = client.get_user(373934947091742721)
            await user.send(f"{member} just joined the Room 2!")

        elif after.channel.id == 699342733487243291 and member == client.get_user(519894723352199198):
            user = client.get_user(373934947091742721)
            await user.send(f"{member} just joined the Room 3!")

    if after.channel is None and member == client.get_user(519894723352199198):
        user = client.get_user(373934947091742721)
        await user.send(f"{member} just left the room!\n----------------------------")


@client.command()
async def help(ctx):
	embed=discord.Embed(colour=0x520081,title="MeinBot Help",url="https://google.com", description=":tools:  Commands list [here](https://google.com)\n\n :interrobang:  Any questions? [FAQ](https://google.com)\n\n:desktop:  Join our Discord! [Discord server](https://google.com)")
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
async def currency(ctx, amount, frm, to):
	x = convert(frm, to, float(amount))
	y = json.loads(x)
	frm1 = y['from']
	to1 = y['to']
	amount1 = y['amount']
	cnvrtd1 = y['converted']
	embed = discord.Embed(colour=0x520081, title="Currency Converter")
	embed.set_thumbnail(url="https://w7.pngwing.com/pngs/712/357/png-transparent-exchange-rate-currency-computer-icons-foreign-exchange-market-coin-coin-text-logo-exchange.png")
	embed.add_field(name="Original:", value=f"{amount} {frm1}")
	embed.add_field(name="Converted:", value=f"{amount1} {to1}")
	await ctx.send(embed=embed)


@currency.error
async def currency_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title="Error", description=f"You need to specify amount and currency from and currency to `.currency 10 eur usd`",colour=0x520081)
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
async def lyrics(ctx, artist, *, music):
	genius = lyricsgenius.Genius(token_genius)
	song = genius.search_song(music, artist)
	per_page = 1000
	pages = math.ceil(len(song.lyrics) / per_page)
	cur_page = 1
	chunk = song.lyrics[:per_page]
	embed = discord.Embed(colour=0x520081)
	embed.add_field(name=f"{music} by {artist}", value=chunk, inline=False)
	embed.add_field(name="Page", value=f"{cur_page}/{pages}", inline=False)
	message = await ctx.send(embed=embed)
	#message = await ctx.send(f"Page {cur_page}/{pages}:\n{chunk}")
	await message.add_reaction("◀️")
	await message.add_reaction("▶️")
	active = True
	
	def check(reaction, user):
		return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

	while active:
		reaction, user = await client.wait_for("reaction_add", check=check)
			
		if str(reaction.emoji) == "▶️" and cur_page != pages:
			cur_page += 1

			if cur_page != pages:
				chunk = song.lyrics[(cur_page-1)*per_page:cur_page*per_page]
			else:
				chunk = song.lyrics[(cur_page-1)*per_page:]
			
			embed = discord.Embed(colour=0x520081)
			embed.add_field(name=f"{music} by {artist}", value=chunk, inline=False)
			embed.add_field(name="Page", value=f"{cur_page}/{pages}", inline=False)
			await message.edit(embed=embed)
			await message.remove_reaction(reaction, user)
				
		elif str(reaction.emoji) == "◀️" and cur_page > 1:
			cur_page -= 1
			chunk = song.lyrics[(cur_page-1)*per_page:cur_page*per_page]
			embed = discord.Embed(title=f"{music}", colour=0x520081)
			embed.add_field(name=f"{music} by {artist}", value=chunk, inline=False)
			embed.add_field(name="Page", value=f"{cur_page}/{pages}", inline=False)
			await message.edit(embed=embed)
			#await message.edit(content=f"Page {cur_page}/{pages}:\n{chunk}")
			await message.remove_reaction(reaction, user)


@lyrics.error
async def lyrics_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title="Error", description=f"You need to specify song and artist `.lyrics \"Dua Lipa\"`",colour=0x520081)
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
        embed = discord.Embed(title="Error", description=f"You need to specify instagram profile `.ig selenagomez`",colour=0x520081)
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
        embed = discord.Embed(title="Error", description=f"You need to specify google search `.google Elon Musk`",colour=0x520081)
        await ctx.send(embed=embed)


@client.command(aliases=['w'])
async def wiki(ctx, *, question):
	try:
		a = wikipedia.summary(question)
		per_page = 1000
		pages = math.ceil(len(a) / per_page)
		cur_page = 1
		chunk = a[:per_page]
		embed = discord.Embed(colour=0x520081)
		embed.set_thumbnail(url="https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png")
		embed.add_field(name="Wikipedia", value = chunk)
		embed.add_field(name="Page", value=f"{cur_page}/{pages}", inline=False)
		message = await ctx.send(embed=embed)
		await message.add_reaction("◀️")
		await message.add_reaction("▶️")
		active = True
		
		def check(reaction, user):
			return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

		while active:
			reaction, user = await client.wait_for("reaction_add", check=check)
				
			if str(reaction.emoji) == "▶️" and cur_page != pages:
				cur_page += 1

				if cur_page != pages:
					chunk = a[(cur_page-1)*per_page:cur_page*per_page]
				else:
					chunk = a[(cur_page-1)*per_page:]
				
				embed = discord.Embed(colour=0x520081)
				embed.set_thumbnail(url="https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png")
				embed.add_field(name="Wikipedia", value = chunk)
				embed.add_field(name="Page", value=f"{cur_page}/{pages}", inline=False)
				await message.edit(embed=embed)
				await message.remove_reaction(reaction, user)
					
			elif str(reaction.emoji) == "◀️" and cur_page > 1:
				cur_page -= 1
				chunk = a[(cur_page-1)*per_page:cur_page*per_page]
				embed = discord.Embed(colour=0x520081)
				embed.set_thumbnail(url="https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png")
				embed.add_field(name="Page", value=f"{cur_page}/{pages}", inline=False)
				embed.add_field(name="Wikipedia", value = chunk)
				await message.edit(embed=embed)
				#await message.edit(content=f"Page {cur_page}/{pages}:\n{chunk}")
				await message.remove_reaction(reaction, user)
				
	except Exception as e:
		embed = discord.Embed(colour=0x520081)
		embed.set_thumbnail(url="https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png")
		embed.add_field(name="I didn\'t find anything like that try: ", value= e)
		await ctx.send(embed=embed)

@wiki.error
async def wiki_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title="Error", description=f"You need to specify wiki search `.wiki \"Donald Trump\"`", colour=0x520081)
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
        await ctx.channel.send("Cannot find this country.Try using .countries")

@corona.error
async def corona_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title="Error", description=f"You need to specify a country `.corona US`",colour=0x520081)
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
        embed = discord.Embed(title="Error", description=f"You need to specify word to be translated `.translate Okno`",colour=0x520081)
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
    role = get(member.guild.roles, name="Peasant")
    await member.add_roles(role)
    channel = client.get_channel(id=747512532930920588)
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


client.run(token)

