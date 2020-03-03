import discord
from datetime import datetime
import os

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_voice_state_update(member, before, after):
    alert_channel = client.get_channel(684293450954178585)
    if before.channel is None:
        msg = f'{member.name}さんがおべんきょうを始めました。がんばって！'
        await alert_channel.send(msg)
        dt1 = datetime.now()
        await alert_channel.send(dt1)
    elif after.channel is None:
        msg = f'{member.name}さんお疲れさまでした！'
        await alert_channel.send(msg)

client.run(token)
