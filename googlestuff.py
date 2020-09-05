import discord
import json
from discord.ext import commands
from googlesearch import search
from google_currency import convert
from googletrans import Translator

class GoogleStuff(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def google(self, ctx,*, query):
        await ctx.send("I'm searching google...")
        for i in search(query,lang='en',num=1,start=0,stop=1,pause=2):
            i1 = i
        for i in search(query,lang='en',num=1,start=0,stop=2,pause=2):
            i2 = i

        for i in search(query,lang="en",num=1,start=0,stop=3,pause=2):
            i3=i

        await ctx.channel.purge(limit=1)
        embed = discord.Embed(colour=0x520081)
        embed.set_thumbnail(url="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
        embed.set_author(name="Google Search")
        embed.add_field(name="1. Result", value=i1,inline=False)
        embed.add_field(name="2. Result", value=i2,inline=False)
        embed.add_field(name="3. Result", value=i3,inline=False)
        await ctx.send(embed=embed)

    @google.error
    async def search_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description=f"You need to specify google search `.google Elon Musk`",colour=0x520081)
            await ctx.send(embed=embed)

    @commands.command()
    async def currency(self, ctx, amount, frm, to):
        x = convert(frm, to, float(amount))
        y = json.loads(x)
        frm1 = y['from']
        to1 = y['to']
        amount1 = y['amount']
        cnvrtd1 = y['converted']
        embed = discord.Embed(colour=0x520081, title="Currency Converter")
        embed.set_thumbnail(url="https://w7.pnging.com/pngs/712/357/png-transparent-exchange-rate-currency-computer-icons-foreign-exchange-market-coin-coin-text-logo-exchange.png")
        embed.add_field(name="Original:", value=f"{amount} {frm1}")
        embed.add_field(name="Converted:", value=f"{amount1} {to1}")
        await ctx.send(embed=embed)

    @currency.error
    async def currency_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description=f"You need to specify amount and currency from and currency to `.currency 10 eur usd`",colour=0x520081)
            await ctx.send(embed=embed)

    @commands.command(aliases=['t', 'tr', 'trns'])
    async def translate(self, ctx, word: str, scnd_l: str="en"):
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
    async def translate_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description=f"You need to specify word to be translated `.translate Okno`",colour=0x520081)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(GoogleStuff(client))

    
'''

d = {}
output = ""

for i in search(query="LOL",num=10,stop=10,pause=2):
    output = output + i

print(output)'''