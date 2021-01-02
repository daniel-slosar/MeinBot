import os
import discord
from discord.ext import commands
import wikipedia
import math
import lyricsgenius
import instaloader

token_genius = open("D:\\Python\\MeinBot\\genius_token.txt", "r").read()

class Social(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['w'])
    async def wiki(self, ctx, *, question):
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
            embed.set_footer(text=f"Powered by https://pypi.org/project/wikipedia/")
            message = await ctx.send(embed=embed)
            await message.add_reaction("◀️")
            await message.add_reaction("▶️")
            active = True
            
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

            while active:
                reaction, user = await self.client.wait_for("reaction_add", check=check)
                    
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
    async def wiki_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description=f"You need to specify wiki search `.wiki \"Donald Trump\"`", colour=0x520081)
            await ctx.send(embed=embed)


    @commands.command()
    async def lyrics(self, ctx, artist, *, music):
        try:
            genius = lyricsgenius.Genius(token_genius)
            song = genius.search_song(music, artist)
        except:
            await ctx.send("FUUUUUCK")

        per_page = 1000
        pages = math.ceil(len(song.lyrics) / per_page)
        cur_page = 1
        chunk = song.lyrics[:per_page]
        embed = discord.Embed(colour=0x520081)
        embed.add_field(name=f"{music.capitalize()} - {artist.capitalize()}", value=chunk, inline=False)
        embed.add_field(name="Page", value=f"{cur_page}/{pages}", inline=False)
        embed.set_footer(text = f"Powered by: https://pypi.org/project/lyricsgenius/")
        message = await ctx.send(embed=embed)
        #message = await ctx.send(f"Page {cur_page}/{pages}:\n{chunk}")
        await message.add_reaction("◀️")
        await message.add_reaction("▶️")
        active = True
        
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

        while active:
            reaction, user = await self.client.wait_for("reaction_add", check=check)
                
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
    async def lyrics_error(self,ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description=f"You need to specify song and artist `.lyrics Baby Justin Bieber` or `.lyrics \"Dua Lipa\" Levitating`",colour=0x520081)
            await ctx.send(embed=embed)


    @commands.command()
    async def ig(self, ctx, profile):
        profile1 = profile
        instg = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(instg.context, profile)
        instg.context.get_and_write_raw(profile.profile_pic_url, "instagram.jpg")
        await ctx.channel.send(f"<https://www.instagram.com/{profile1}/>")
        await ctx.channel.send(file=discord.File('instagram.jpg'))

    @ig.error
    async def ig_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = discord.Embed(title="Error", description=f"You need to specify instagram profile `.ig selenagomez`",colour=0x520081)
            await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        embed=discord.Embed(colour=0x520081,title="AVATAR")
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Social(client))