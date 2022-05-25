from keep_alive import keep_alive
import discord
import os
import requests
import json
import random
import sys
import platform
import coroutine
from replit import db
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import tasks
import asyncio

client = discord.Client()

bot = Bot(command_prefix="!")

#bot = Bot("$")

#bot = commands.Bot(command_prefix='!')

#bot = commands.Bot(command_prefix='$')

whatcanido = "```Sziasztok, Hali <Szia!>\nMedve <Sziasztok!>\nKincső <Itt mindenki függő?!>\nSvéd <Svéd katonák harcra fel!>\n;vicc <random kép, videó>\n Inspire <inspiráció>```"

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements

#@client.event
#async def on_ready():
#  print("We have logged in as {0.user}".format(client))

#PREFIX = ("$")

#bot = commands.Bot(command_prefix=PREFIX, description='Hi')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Bot by _B[-RCł_#3387'))

#@bot.event
#async def on_ready():
#  game = discord.Game('berci')
#  await client.change_presence(status=discord.Status.idle, activity=game)


#@bot.event
#async def on_ready():
#  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

#randomnumber start

#bot = commands.Bot(command_prefix='!')

@bot.command()
async def givenum(ctx):

    # checks the author is responding in the same channel
    # and the message is able to be converted to a positive int
    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit() and \
               msg.channel == ctx.channel

    await ctx.send("Type a number")
    msg1 = await client.wait_for("message", check=check)
    await ctx.send("Type a second, larger number")
    msg2 = await client.wait_for("message", check=check)
    x = int(msg1.content)
    y = int(msg2.content)
    if x < y:
        value = random.randint(x,y)
        await ctx.send(f"You got {value}.")
    else:
        await ctx.send(":warning: Please ensure the first number is smaller than the second number.")

#randomnumber end

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  inspire = ["Inspire", "inspire"]
  
  await bot.process_commands(message)
  
  if any(word in msg for word in inspire):
    quote = get_quote()
    await message.channel.send(quote)

  if message.author == client.user:
        return

  inspir3 = ["inspiráció", "Inspiráció"]

  if any(word in msg for word in inspir3):
        await message.channel.send('Csak tedd a lehető legjobban. Ennél többet senki sem tehet -John Wooden')

  medve = ["medve", "Medve"]

  if any(word in msg for word in medve):
        await message.channel.send('Sziasztok!')

  hali = ["hali", "Hali"]

  if any(word in msg for word in hali):
        await message.channel.send('Szia!')

  sziasztok = ["sziasztok", "Sziasztok"]

  if any(word in msg for word in sziasztok):
        await message.channel.send('Szia!')

  if message.content.startswith('svéd'):
        await message.channel.send('Svéd katonák harcra fel!')

  if message.content.startswith('Svéd'):
        await message.channel.send('Svéd katonák harcra fel!')

  if message.content.startswith('kincső'):
        await message.channel.send('"itt mindenki függő!?"')

  if message.content.startswith(';vicc'):
    path = random.choice(os.listdir("vicc/"))
    await message.channel.send(file=discord.File("vicc/"+path))

  if message.content.startswith(';help'):
        await message.channel.send(whatcanido)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
    
  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

@bot.command(name = "ping") 
async def rohadt(ctx): await ctx.channel.send("pong")

keep_alive()
client.run(os.environ['TOKEN'])