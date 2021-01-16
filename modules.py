import os
import discord
import datetime
import json
from covid import Covid
import random
import imdb
from discord.ext import commands


class Modules(commands.Cog):

    def __init__(self, client):
        self.client = client

    

    @commands.command()
    async def days(self, ctx, days):
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
    async def days_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description=f"You need to specify number as days `.days 356`",colour=0x520081)
            await ctx.send(embed=embed)


    @commands.command()
    async def corona(self,ctx, krajina):
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
            embed.add_field(name="Powered by: ", value="https://pypi.org/project/covid/")
            await ctx.channel.send(embed=embed)
        except:
            await ctx.channel.send(f"Cannot find this country, maybe try `.corona \"Dominican Republic\"` or try using `.countries`")

    @corona.error
    async def corona_error(self,ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description=f"You need to specify a country `.corona USA`",colour=0x520081)
            await ctx.send(embed=embed)
        
    
    @commands.command()
    async def movie(self,message):
        global meinbot_guild
        im = imdb.IMDb()
        search = im.get_top250_movies()
        i = random.randint(1,250)
        embed = discord.Embed(colour=0x520081)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/1200px-IMDB_Logo_2016.svg.png")
        embed.add_field(name="Movie you should watch: ", value=search[i], inline = True)
        embed.add_field(name="Powered by: ", value="https://pypi.org/project/IMDbPY/")
        embed.set_footer(text="https://www.imdb.com/") 
        await message.channel.send(embed=embed)
        

def setup(client):
    client.add_cog(Modules(client))