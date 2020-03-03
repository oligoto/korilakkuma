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

        msg = f'{member.name} さんがお勉強をはじめました。がんばって！'
        await alert_channel.send(msg)

        dt1 = datetime.datetime.now()

    elif after.channel is None:
        duration_time = datetime.datetime.now() + datetime.timedelta(-dt1)
        duration_time_adjust = int(duration_time.total_seconds()) * -1

        msg = f'{member.name} さんが {duration_time_adjust} 秒 お勉強しました。お疲れさまでした！'
        await alert_channel.send(msg)

client.run(token)
