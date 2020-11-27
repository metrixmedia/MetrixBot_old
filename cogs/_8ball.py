import discord
import random
from discord.ext import commands


class _8ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='8ball', aliases=['ask', 'boulemagique'])
    async def _8ball(ctx, *, question): 
        responses = ['J\'ai de sérieux doutes.',
                     'On dirait bien.',
                     'C\'est assez probable.',
                     'C\'est non.',
                     'Peu probable',
                     'Faut pas rêver.',
                     'N\'y compte pas.',
                     'Impossible !',
                     'D\'après moi oui',
                     'C\'est certain !',
                     'Oui absolument !',
                     'Tu peux compter dessus',
                     'Sans aucun doute',
                     'Très probable',
                     'Oui',
                     'C\'est bien parti !',
                     'Répète ta question !',
                     'Mdr, peut-être... Qui sait ?']
        await ctx.send(f'question: {question}\nRéponse : {random.choice(responses)}')
        return

def setup(client):
    client.add_cog(_8ball(client))