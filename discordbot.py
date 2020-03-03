import discord
import os
import datetime

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_voice_state_update(before, after):
    if nowtime = nowtime + datetime.timedelta(hours=9)
nowtime = nowtime.strftime("%m/%d-%H:%M")
vcchannel = client.get_channel('time')
 
if(before.voice_channel is None):
    jointext=nowtime + "に　" + after.name + "　が　" + after.voice_channel.name + " に参加しました。"
    await client.send_message(vcchannel, jointext)
elif(after.voice_channel is None):
    outtext=nowtime + "に " + before.name + "　が　" + before.voice_channel.name + " から退出しました。"
    await client.send_message(vcchannel, outtext)

client.run(token)
