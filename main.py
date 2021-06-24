import discord
from discord.ext import commands
import json

# configuration.json dosyasından veri alma
with open("configuration.json", "r") as config: 
	data = json.load(config)
	token = data["token"]
	prefix = data["prefix"]


class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

# intent kısmı değiştirmeyin
intents = discord.Intents.default()
# botun tanımı
bot = commands.Bot(prefix, intents = intents)

# cogs dosyasındaki komutları yükleme
if __name__ == '__main__':
	for filename in os.listdir("Cogs"):
		if filename.endswith(".py"):
			bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
	print(f"Giriş yapıldı! {bot.user}")
	print(discord.__version__)
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"Developed by Ponche#6600")) # Burayı değişrirebilirsiniz.

bot.run(token)