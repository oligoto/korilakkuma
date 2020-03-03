import discord
from datetime import datetime, timedelta

client = discord.Client()

@client.event
async def on_voice_state_update(member, before, after):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(time)
        if before.channel is None:
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)
        elif after.channel is None:
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {before.channel.name} から退出しました。'
            await alert_channel.send(msg)

client.run("Njg0MjgwNDM3NzkwNjA1MzEy.Xl4Zlg.ND3o7NVNkuUsTE6bZj-HrpxBxiI")
