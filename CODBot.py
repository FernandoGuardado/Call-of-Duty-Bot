import random
import os
import discord
from discord.ext import commands

def countMaps(lst, x): 
    count = 0
    for ele in lst: 
        if (ele == x): 
            count = count + 1
    return count 

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command(aliases=['8s'])
async def map8s(ctx):
    search = ['Raid', 'Crossroads', 'Moscow', 'Garrison', 'Miami', 'Checkmate']
    hardpoint = ['Crossroads', 'Checkmate', 'Garrison', 'Raid']
    control = ['Raid', 'Checkmate', 'Garrison']
    mapPool = []

    firstMap = random.randint(0, 3)
    mapPool.append(hardpoint[firstMap])

    secondMap = random.randint(0,5)
    mapPool.append(search[secondMap])

    while True:
        thirdMap = random.randint(0,2)
        mapCount = countMaps(mapPool, control[thirdMap])

        if mapCount < 2:
            mapPool.append(control[thirdMap])
            break
        else:
            continue

    while True:
        fourthMap = random.randint(0, 3)
        if firstMap == fourthMap:
            continue
        else:
            mapCount = countMaps(mapPool, hardpoint[fourthMap])

            if mapCount < 2:
                mapPool.append(hardpoint[fourthMap])
                break
            else:
                continue
    while True:
        fifthMap = random.randint(0,5)
        if secondMap == fifthMap:
            continue
        else:
            mapCount = countMaps(mapPool, search[fifthMap])

            if mapCount < 2:
                mapPool.append(search[fifthMap])
                break
            else:
                continue

    await ctx.send(f'{mapPool[0]}\n{mapPool[1]}\n{mapPool[2]}\n{mapPool[3]}\n{mapPool[4]}')

@client.command(aliases=['flip'])
async def coinFlip(ctx):
    flip = random.randint(0,1)

    if flip == 0:
        await ctx.send(':coin: Heads')
    else:
        await ctx.send(':coin: Tails')

client.run(os.environ['DiscordToken'])