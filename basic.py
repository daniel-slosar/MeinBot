import os
import discord
import time
from discord.ext import commands
import random

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(colour=0x520081, title="Ping")
        embed.add_field(name="Latency:", value=self.client.latency)
        await ctx.send(embed=embed)


    @commands.command()
    async def repeat(self,ctx, *, msng):
        if msng == "I\'m stupid":
            await ctx.send("Yeah, we know..")
        elif msng == "I suck dicks":
            await ctx.send("Yes you do!")
        else:
            await ctx.send(msng)

    @repeat.error
    async def repeat_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description=f"What should I repeat? `.repeat Hello!`",colour=0x520081)
            await ctx.send(embed=embed)

        
    @commands.command()
    async def poke(self, ctx,user,n: int=1):
        await ctx.channel.purge(limit=1)
        for n in range(n):
            time.sleep(0.8)
            await ctx.send(f"{user}")

def setup(client):
    client.add_cog(Basic(client))