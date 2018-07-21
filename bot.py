import discord 
from discord.ext import commands 
import random
from discord.voice_client import VoiceClient

startup_extensions = ["Music"]

# from app bot user 
# click to reveal 
TOKEN = 'token_here'

# set prefix 
bot = commands.Bot(command_prefix = '!')

# intialize 
@bot.event 
async def on_ready():
	print('bot online')

class Main_Commands():
	def __init__(self, bot):
		self.bot = bot

# commands 
@bot.command()
async def flip():
	flip = random.choice(['heads', 'tails'])
	await bot.say(flip)
	
@bot.command(pass_context = 1)
async def roles(context):
	rolls = context.message.server.roles
	result = 'the roles are '
	for role in rolls:
		result += role.name + '. ' 
	await bot.say(result)

@bot.command(pass_context = 1)
async def num10(context):
	num = random.randint(1, 10)
	await bot.say(num)

# music 
if __name__ == "__main__":
	for extension in startup_extensions:
		try: 
			bot.load_extension(extension)
		except Exception as e: 
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extensions {}\n{}'.format(extension, exc))

# events 
@bot.event
async def on_message(message):
	if message.content.upper().startswith('NIGGER'):
		await bot.send_message(message.channel, "Please do not use that word here.")
	
	await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    await bot.change_presence(game=discord.Game(name='Hi %s' % (member)))
    await bot.send_message(member, "Hi %s, Welcome to Carson's Discord Server! This server is fairly NSFW at times; you've been warned! Enjoy your stay :)" % (member))

@bot.event
async def on_member_remove(member):
    await bot.change_presence(game=discord.Game(name='Bye %s' % (member)))

# execute bot
bot.run(TOKEN)