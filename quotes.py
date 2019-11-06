#!/usr/bin/env python3

# https://discordapp.com/oauth2/authorize?client_id=633799032862408704&permissions=8&scope=bot

import discord
import wikiquotes

from discord.ext import commands

client = commands.Bot(command_prefix="<")

token = 'NjMzNzk5MDMyODYyNDA4NzA0.XaZOZw.dx57LUhi7gbeMnaY2YBhbJdVwO0'

@client.event
async def on_ready():
    print("Bot is online.")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Type <usage for help."))

@client.event
async def on_message(message):
    if message.content.startswith("<usage"):
        await message.channel.send("Type `<search author-name` to search for an author. Type `<day` to display the Wikiquotes quote of the day.")

    if message.content.startswith("<day"):
        await message.channel.send(wikiquotes.quote_of_the_day("english"))

    if message.content.startswith("<pacer"):
        await message.channel.send("""The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly but gets faster each minute after you hear this signal. A single lap should be completed every time you hear this sound. Remember to run in a straight line and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark. Get ready!… Start.""")

    await client.process_commands(message)

@client.command(pass_context=True)
async def search(ctx, author):
    await ctx.send(wikiquotes.random_quote(author, "english"))

client.run(token)
