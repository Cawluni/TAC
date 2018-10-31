# Note that discord.py is in async to allow things to happen together/at the same time. use async for all functions.

import discord,json #,socket,inspect
from discord.ext import commands


ownerID = "133344122986561537"
whitelist= ["170583150731198464"] # This is a bypass for any commands for any reason-usually bot owner only commands
etern = "170583150731198464"

bot = commands.Bot(command_prefix="~",description="",pm_help=True)
bot.remove_command('help')

ext = [] # No cogs at this time
### Load up cogs ###
if __name__ == '__main__':
    for extension in ext:
      try:
        bot.load_extension(extension)
      except Exception as e:
        a = ("Failed to load extension {}\n{}: {}".format(extension, type(e).__name__, e))
        print(a)

# Get bot on ready status #
@bot.event
async def on_ready():
  print("BOT ONLINE")
  await bot.change_presence(game=discord.Game(name='~help |TAC v2'))
  #for server in bot.servers:
    #print(server.name) # This just prints the server lists


# Built In Functions here.
async def update_data(users, user):
  if not user.id in users:
    users[user.id] = {}
    users[user.id]['XP'] = 0
    users[user.id]['level'] = 1
 
async def add_user(economy, user):
    bank = economy['user data ']
    if not user.id in bank:
      bank[user.id] = {}
      bank[user.id]['Balance'] = 0
      bank[user.id]['Debt'] = 0
      bank[user.id]['Inventory'] = []
      
    
    
    
async def addXP(users, user, exp):
  users[user.id]['XP'] += exp


async def lvl_up(users, user, channel):
  xp = users[user.id]['XP']
  lvl_start = users[user.id]['level']
  lvl_end = int(xp ** (1/4))

  if lvl_start < lvl_end:
    await bot.send_message(channel, "{} has leveled up to level {}!".format(user.mention, lvl_end))
    users[user.id]['level'] = lvl_end

async def addBalance(users, user, ammount ):
  pass
# Bot Related Here v

# Commands # 
@bot.command(pass_context=True)
async def help(ctx): #  With embeds soon to come/being made
  user = ctx.message.author
  pageOne = discord.Embed(
    title = 'Page One',
    description = 'TAC bot commands pg. 1 of 1',
    colour = discord.Colour.red()
  )
  pageOne.set_footer(text="Page 1 of 1")
  if user is not None: 
      await bot.send_message(user,pageOne=pageOne)
      await bot.say("Hey I sent you the commands in DMS")


# Music # Should I make this an extention?
@bot.command()
async def play(ctx,*,song=None): # Because song is none, this takes a few different routes.
  
  pass
# Bot Functions

@bot.event
async def on_member_join(member):
  with open('levels.json','r') as f:
    users = json.load(f)
  
  with open('economy.json','r') as e:
    economy = json.load(e)

  await add_user(economy, member)
  await update_data(users, member)
  
  

  with open('levels.json','w') as f:
    json.dump(users, f)  


logs = open("chat_logs.json",'w')
@bot.listen()
async def on_message(message):
  auth = message.author
  content = message.content
  print("{}:{}".format(auth,content)) 
  json.dump("{}:{}".format(auth,content),logs)
  
  with open('levels.json','r') as f:
    users = json.load(f)

  await update_data(users, message.author)
  await addXP(users, message.author, 5)
  await lvl_up(users, message.author, message.channel)

  with open('levels.json','w') as f:
    json.dump(users, f)  
  ### 
  # Take this information
# Run bot
bot.run('NTA0MDM1MzE4ODA3MTM0MjEw.Dq_Zkw.fwxMy0nr0Va4Nk-SQpCw9-wqFm0')