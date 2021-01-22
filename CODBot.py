import random
import os
import discord
from discord import colour
from discord.ext import commands

def countMaps(lst, x): 
    count = 0
    for ele in lst: 
        if (ele == x): 
            count = count + 1
    return count 

client = commands.Bot(command_prefix = '!')

# log that bot is ready when put online
@client.event
async def on_ready():
    print('Bot is ready')

# command to create bo5 map pool for 8s
@client.command(aliases=['8s'])
async def map8s(ctx):
    search = ['Raid', 'Crossroads', 'Moscow', 'Garrison', 'Miami', 'Checkmate']
    hardpoint = ['Crossroads', 'Checkmate', 'Garrison', 'Raid', 'Moscow']
    control = ['Raid', 'Checkmate', 'Garrison']
    mapPool = []

    firstMap = random.randint(0, 4)
    mapPool.append(hardpoint[firstMap])

    while True:
        secondMap = random.randint(0,5)
        mapCount = countMaps(mapPool, search[secondMap])

        if mapCount < 1:
            mapPool.append(search[secondMap])
            break

    while True:
        thirdMap = random.randint(0,2)
        mapCount = countMaps(mapPool, control[thirdMap])

        if mapCount < 1:
            mapPool.append(control[thirdMap])
            break

    while True:
        fourthMap = random.randint(0, 4)
        if firstMap == fourthMap:
            continue
        else:
            mapCount = countMaps(mapPool, hardpoint[fourthMap])

            if mapCount < 2:
                mapPool.append(hardpoint[fourthMap])
                break
    while True:
        fifthMap = random.randint(0,5)
        if secondMap == fifthMap:
            continue
        else:
            mapCount = countMaps(mapPool, search[fifthMap])

            if mapCount < 1:
                mapPool.append(search[fifthMap])
                break

    # await ctx.send(f'{mapPool[0]}\n{mapPool[1]}\n{mapPool[2]}\n{mapPool[3]}\n{mapPool[4]}')
    embed = discord.Embed(
        title = 'Best of 5 Series:',
        colour = discord.Colour.teal()
    )
    embed.add_field(name='Hardpoint', value=mapPool[0], inline=False)

# command to flip a coin
@client.command(aliases=['flip'])
async def coinFlip(ctx):
    flip = random.randint(0,1)

    if flip == 0:
        await ctx.send(':coin: Heads')
    else:
        await ctx.send(':coin: Tails')

# grab discord token from heroku and run bot
client.run(os.environ['DiscordToken'])