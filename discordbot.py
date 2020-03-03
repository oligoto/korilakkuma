import discord
from datetime import datetime, timedelta
import os

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_voice_state_update(member, before, after):
    now = datetime.utcnow() + timedelta(hours=9)
    alert_channel = client.get_channel(684293450954178585)
    if before.channel is None:
        
        pretime_dict[after.name] = datetime.datetime.now()
        
        msg = f'{member.name} さんがお勉強を始めました。がんばって！'
        await alert_channel.send(msg)
    elif after.channel is None:
        duration_time = pretime_dict[before.name] - datetime.datetime.now()
        duration_time_adjust = int(duration_time.total_seconds()) * -1

        msg = f'{member.name} さんが {duration_time_adjust} 秒お勉強しました。お疲れ様でした！'
        await alert_channel.send(msg)

client.run(token)
