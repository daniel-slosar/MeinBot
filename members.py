import os
import discord
import time
import platform
from discord.ext import commands

class Members(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def info(self, ctx):
        pltf = platform.platform()
        embed = discord.Embed(colour=0x520081, title="INFO",timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(name="Name: ", value="MeinBot#1050")
        embed.add_field(name="Creation date: ", value="01 May 2019")
        embed.add_field(name="Created by: ", value="01001100#2651")
        embed.add_field(name="Running on: ", value=pltf)
        embed.add_field(name="Help command:", value=f"`.help`")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def userinfo(self,ctx, member: discord.Member = None):
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

    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        server_id = guild.id
        print(guild)
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                pltf = platform.platform()
                member = self.client.get_user(573091512066375690)
                await channel.send("Hi, my name is MeinBot. I\'m your new bot!")
                embed = discord.Embed(colour=0x520081, title="INFO")
                embed.set_thumbnail(url=member.avatar_url)
                embed.add_field(name="Name: ", value="MeinBot#1050")
                embed.add_field(name="Creation date: ", value="01 May 2019")
                embed.add_field(name="Created by: ", value="01001100#2651")
                embed.add_field(name="Running on: ", value=pltf)
                embed.add_field(name="Help command: ", value=f"`.command`")
                embed.add_field(name="Programming language: ", value=f"Python 3.7")
                await channel.send(embed=embed)
                await channel.send("Set your default role by typing `.role yourrolehere`")
                break

def setup(client):
    client.add_cog(Members(client))