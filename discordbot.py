import discord
from datetime import datetime
import os

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()
pretime_dict = {}

@client.event
async def on_voice_state_update(member, before, after):
    alert_channel = client.get_channel(684293450954178585)
    if before.channel is None:

        dt1 = datetime.datetime.now()
        msg = f'{member.name} さんがお勉強をはじめました。がんばって！'
        await alert_channel.send(msg, dt1)

    elif after.channel is None:
        dt2 = datetime.datetime.now()
        delta = dt2 - dt1

        msg = f'{member.name} さんが {delta.total_seconds()} 秒 お勉強しました。お疲れさまでした！'
        await alert_channel.send(msg)

client.run(token)
