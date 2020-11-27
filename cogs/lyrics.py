import discord
from discord.ext import commands
import lyricwikia
from replit import db



class Lyrics(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def lyrics(self, ctx): 
        await ctx.send(lyrics = lyricwikia.get_lyrics(value = db["music"]))

        return



def setup(client):
    client.add_cog(Lyrics(client))