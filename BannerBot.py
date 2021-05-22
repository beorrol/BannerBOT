import discord, time
import asyncio
import aiohttp
from discord_webhook import DiscordWebhook, DiscordEmbed

content = """
@everyone
"""
prefix = "-"
minute = 30

embed = DiscordEmbed()
embed.set_title("Title")
embed.set_description("Description")

# embed = None



intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(client.user)
    await client.change_presence(activity=discord.Game(f"{prefix}배너추가 [WebhookURL]"))
    while True:
        with open("webhook.txt", "r", encoding='utf8') as fp:
            webhooks = fp.read().split("\n")
        for i in webhooks:
            webhook = DiscordWebhook(url=i, content=content)
            if embed != None:
                webhook.add_embed(embed=embed)
            response = webhook.execute()
        time.sleep(minute * 60)

@client.event
async def on_message(msg: discord.Message):
    if msg.author.bot: return
    if msg.content.startswith(f"{prefix}배너추가"):
        role = discord.utils.get(msg.guild.roles, name="배너직원")
        if not role in msg.author.roles:
            return
        webhook = msg.content.split(" ")[0]
        with open("webhook.txt", "a", encoding='utf8') as fp:
            fp.write(f"{webhook}\n")



client.run("")