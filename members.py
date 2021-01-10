import os
import discord
import time
import datetime
import platform
from discord.ext import commands
from discord.utils import get

global ROLE

class Members(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()#needable
    async def role(self, ctx, role):
        global server_id
        server_id = ctx.message.guild.id
        print(server_id)
        global ROLE
        ROLE = role
        print(ROLE)

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
        embed.add_field(name="Bot", value=member.bot)
        embed.add_field(name="Created at:", value=member.created_at.strftime("%A \n %d %B %Y \n %H:%M:%S:%f")[:-3])
        embed.add_field(name="Joined at server:", value=member.joined_at.strftime("%A \n %d %B %Y \n %H:%M:%S:%f")[:-3])
        embed.add_field(name=f"Roles ({len(roles)}):", value=" ".join([role.mention for role in roles]), inline=False)
        await ctx.send(embed=embed)

    @userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(title="Error", description=f"This member does not exist!",colour=0x520081)
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
                embed.add_field(name="Help command: ", value=f"`.help")
                embed.add_field(name="Programming language: ", value=f"Python 3.7")
                await channel.send(embed=embed)
                await channel.send("Set your default role by typing `.role yourrolehere`")
                break

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.raw_status == "offline" and after.raw_status == "online" and int(before.id) == 472502168738463755:
            user = self.client.get_user(373934947091742721)
            member = self.client.get_user(472502168738463755)
            timenow = datetime.datetime.now()
            await user.send(f"**```yaml\n{member} is Online!\nTime: {timenow.strftime('%R')}```**")

    @commands.Cog.listener()
    async def on_member_join(self,member):
        server_id = member.guild.id
        if server_id == 515156152066244635:
            print("GermanReich")
            channel = self.client.get_channel(768940272561946645)
            await channel.edit(name = '📊Member count: {}'.format(channel.guild.member_count))
            #channel = client.get_channel(769528310552068106)
            print(member)
            embed = discord.Embed(title="RULES!",colour=0xff0000,url="https://daydream404.github.io/MeinBot/",description="READ THE RULES!\n\n**0000. Respect everyone.\n\n0001. Use channels properly.\n\n0010. Speak only English.\n\n0011. Do not spam.\n\n0100. Do not advertise.\n\n0101. Do not post anything NSFW or you'll get banned.\n\n0110. Do not swear or use abusive language.\n\n0111. Do not start conversation with controversial topics.\n\n1000. Do not mention @everyone.\n\n1001. Do not share any files for download.**\n\nAfter reading the rules confirm accepting them by reacting with :thumbsup:")
            #await channel.send(embed=embed)
            await member.send(embed=embed)
            
            def check(reaction, user):
                return user == member and str(reaction.emoji) in ['👍']
            
            reaction, user = await self.client.wait_for("reaction_add", check=check)
            role = get(member.guild.roles, name="Landwirt")
            await member.add_roles(role)
            meinbot_guild = self.client.get_guild(515156152066244635)
            #meinbot_guild is servername
            #server_id is id
            for channel in meinbot_guild.text_channels:
                if channel.permissions_for(meinbot_guild.me).send_messages:
                    embed = discord.Embed(colour=0x520081, description=f"Welcome to the party!")
                    embed.set_thumbnail(url=f"{member.avatar_url}")
                    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
                    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
                    embed.add_field(name=f"Your role: ", value=role)
                    embed.timestamp = datetime.datetime.now()
                    await channel.send(embed=embed)
                    break

        elif server_id == 751897980432547941:
            print("MeinbotServer")
            channel = self.client.get_channel(768941337927352342)
            await channel.edit(name = '📊Member count: {}'.format(channel.guild.member_count))
            role = get(member.guild.roles, name="noob")
            await member.add_roles(role)
            meinbot_guild = self.client.get_guild(751897980432547941)
            for channel in meinbot_guild.text_channels:
                if channel.permissions_for(meinbot_guild.me).send_messages:
                    embed = discord.Embed(colour=0x520081, description=f"Welcome to the party!")
                    embed.set_thumbnail(url=f"{member.avatar_url}")
                    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
                    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
                    embed.add_field(name=f"Your role: ", value=role)
                    embed.timestamp = datetime.datetime.now()
                    await channel.send(embed=embed)
                    break

        else:
            try:
                role = get(member.guild.roles, name=ROLE)
                await member.add_roles(role)
            except Exception as e:
                await channel.send("Well you fucked up something didn\'t you? Try Help on my [website](https://www.meinbot.com)")   


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        server_id = member.guild.id
        if server_id == 515156152066244635:
            channel = self.client.get_channel(768940272561946645)
            await channel.edit(name = '📊Member count: {}'.format(channel.guild.member_count))

            meinbot_guild = self.client.get_guild(server_id)
            for channel in meinbot_guild.text_channels:
                if channel.permissions_for(meinbot_guild.me).send_messages:
                    embed = discord.Embed(colour=0x520081, description=f"Left the party!")
                    embed.set_thumbnail(url=f"{member.avatar_url}")
                    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
                    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
                    embed.add_field(name=f"We won\'t miss you..", value="Don\'t worry!")
                    embed.timestamp = datetime.datetime.now()
                    await channel.send(embed=embed)
                    break
        
        elif server_id == 751897980432547941:
            channel = self.client.get_channel(768941337927352342)
            await channel.edit(name = '📊Member count: {}'.format(channel.guild.member_count))
            
            meinbot_guild = self.client.get_guild(server_id)
            for channel in meinbot_guild.text_channels:
                if channel.permissions_for(meinbot_guild.me).send_messages:
                    embed = discord.Embed(colour=0x520081, description=f"Left the party!")
                    embed.set_thumbnail(url=f"{member.avatar_url}")
                    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
                    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
                    embed.add_field(name=f"We won\'t miss you..", value="Don\'t worry!")
                    embed.timestamp = datetime.datetime.now()
                    await channel.send(embed=embed)
                    break

        else:
            pass

def setup(client):
    client.add_cog(Members(client))