from events.general import setup
import discord

client = discord.Client()
TOKEN = 'OTE1MjY0MjkzOTM3NzU0MTIy.YaZETA.VsD9bymC4pVMqzJ8fE-RTQG3H7Q'

setup(client)

client.run(TOKEN, bot=True, reconnect=True)
