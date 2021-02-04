import random
import os
import datetime
from typing import Text
import discord
from discord import colour
from discord import message
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
    # await ctx.channel.purge(limit=1)

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

        if mapCount < 2:
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

    embed = discord.Embed(
        colour = discord.Colour.teal()
    )
    embed.add_field(name='Hardpoint', value=mapPool[0], inline=True)
    embed.add_field(name='Search', value=mapPool[1], inline=True)
    embed.add_field(name='Control', value=mapPool[2], inline=True)
    embed.add_field(name='Hardpoint', value=mapPool[3], inline=True)
    embed.add_field(name='Search', value=mapPool[4], inline=True)
    embed.set_footer(text='Powered by Kriptonic')

    await ctx.send(embed=embed)

# command to flip a coin
@client.command(aliases=['flip'])
async def coinFlip(ctx):
    flip = random.randint(0,1)

    if flip == 0:
        embed = discord.Embed(
            title = ':coin: Heads',
            colour = discord.Colour.teal()
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = ':coin: Tails',
            colour = discord.Colour.teal()
        )
        await ctx.send(embed=embed)

# command to display ga rules
@client.command(aliases=['ga'])
async def ga(ctx):
    embed = discord.Embed(
        title = 'Gentlemans Agreements',
        colour = discord.Colour.teal()
    )
    embed.add_field(name='Weapons', value='AK-47\n1911', inline=False)
    embed.add_field(name='Perks/Wildcards', value='Gearhead\nPerk Greed\nLaw Breaker Allowed, No Overkill', inline=False)
    embed.add_field(name='Tacticals', value='Molotovs\nSmokes\n', inline=False)
    embed.add_field(name='Attachments', value='KBG/Socom Eliminator\nDamage Changing Barrels\nThermals\nLasers', inline=False)

    await ctx.send(embed=embed)
# grab discord token from heroku and run bot
client.run(os.environ['DiscordToken'])
