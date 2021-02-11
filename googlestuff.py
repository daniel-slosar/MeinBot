import discord
import json
import requests
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
        '''for i in search(query,lang='en',num=1,start=0,stop=1,pause=2):
            i1 = i
        for i in search(query,lang='en',num=1,start=0,stop=2,pause=2):
            i2 = i

        for i in search(query,lang="en",num=1,start=0,stop=3,pause=2):
            i3=i
        '''
        output=""
        output1 = ""
        for i in search(query,num=5,stop=5,pause=2):
            output = output + i

        output1 = output.split("http")
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(colour=0x520081)
        embed.set_thumbnail(url="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
        embed.set_author(name="Google Search")
        embed.add_field(name="1. Result", value=f"http{output1[1]}",inline=False)
        embed.add_field(name="2. Result", value=f"http{output1[2]}",inline=False)
        embed.add_field(name="3. Result", value=f"http{output1[3]}",inline=False)
        embed.add_field(name="4. Result", value=f"http{output1[4]}",inline=False)
        embed.add_field(name="5. Result", value=f"http{output1[5]}",inline=False)
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

    @commands.command()
    async def crypto(self, ctx, symbol, curr : str="EUR"):
        url = "https://alpha-vantage.p.rapidapi.com/query"
        querystring = {"from_currency":{symbol},"function":"CURRENCY_EXCHANGE_RATE","to_currency":{curr}}
        headers = {
            'x-rapidapi-key': "0b8c1c5c4fmshc448a389a7ab420p1766b6jsn83528d6e5355",
            'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        result = json.loads(response.text)         
        currency_from = result['Realtime Currency Exchange Rate']['2. From_Currency Name']
        currency_to = result['Realtime Currency Exchange Rate']['4. To_Currency Name']
        ex_rate = result['Realtime Currency Exchange Rate']['5. Exchange Rate']
        refresh = result['Realtime Currency Exchange Rate']['6. Last Refreshed']

        embed = discord.Embed(title="Cryptocurrency",colour=0x520081)
        embed.set_thumbnail(url="https://assets.entrepreneur.com/content/3x2/2000/20191217200727-6Crypto.jpeg")
        embed.add_field(name=f"{currency_from}\t= ", value=f"1", inline=True)
        embed.add_field(name=f"{currency_to}", value=f"{ex_rate}", inline=True)
        embed.add_field(name="Last update: ", value=f"{refresh}", inline=False)
        await ctx.send(embed=embed)

    @crypto.error
    async def crypto_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description=f"You need to specify cryptocurrency! Optional you can change currency.. `.crypto BTC USD` or just `.crypto BTC`",colour=0x520081)
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

    