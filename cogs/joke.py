import requests
import discord
from discord.ext import commands

URL = 'https://official-joke-api.appspot.com/random_joke'


def check_valid_status_code(request):
    if request.status_code == 200:
        return request.json()

    return False


def get_joke():
    request = requests.get(URL)
    data = check_valid_status_code(request)

    return data


class Joke(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def joke(self, ctx): 
        await ctx.send(joke = joke.get_joke()
        if joke == False:
            await message.channel.send("Couldn't get joke from API. Try again later.")
        else:
            await message.channel.send(joke['setup'] + '\n' + joke['punchline'])

        return



def setup(client):
    client.add_cog(Joke(client))