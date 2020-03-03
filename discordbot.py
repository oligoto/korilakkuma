import discord
from datetime import datetime
import os

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_voice_state_update(member, before, after):
    now = datetime.utcnow() + timedelta(hours=9)
    alert_channel = client.get_channel(684293450954178585)
    if before.channel is None:
        msg = f'{now:%m/%d-%H:%M}から{member.name}さんがお勉強を始めました。がんばって！'
        await alert_channel.send(msg)
    elif after.channel is None:
        msg = f'{now:%m/%d-%H:%M}まで{member.name}さんがお勉強しました。お疲れさまでした！'
        await alert_channel.send(msg)

client.run(token)
