import random
import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command(aliases=['8s'])
async def _8s(ctx):
    search = ['Raid', 'Crossroads', 'Moscow', 'Garrison', 'Miami', 'Checkmate']
    hardpoint = ['Raid', 'Crossroads', 'Checkmate', 'Garrison']
    control = ['Raid', 'Checkmate', 'Garrison']

    firstMap = random.randrange(0, 3)
    secondMap = random.randrange(0,5)
    thirdMap = random.randrange(0,2)

    while True:
        fourthMap = random.randrange(0, 3)
        if firstMap == fourthMap:
            continue
        else:
            break
    while True:
        fifthMap = random.randrange(0,5)
        if secondMap == fifthMap:
            continue
        else:
            break

    await ctx.send(f'{hardpoint[firstMap]}\n{search[secondMap]}\n{control[thirdMap]}\n{hardpoint[fourthMap]}\n{search[fifthMap]}')

client.run(os.environ['DiscordToken'])