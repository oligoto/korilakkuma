# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'Njg0MjgwNDM3NzkwNjA1MzEy.Xl3z3w.9ASS_30AppRtczHLbwOokSLKOUc'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_voice_state_update(before, after):
  print("ボイスチャンネルで変化がありました")

  if((before.voice.self_mute is not after.voice.self_mute) or (before.voice.self_deaf is not after.voice.self_deaf)):
    print("ボイスチャンネルでミュート設定の変更がありました")
    return

  if(before.voice_channel is None):
    pretime_dict[after.name] = datetime.datetime.now()
  elif(after.voice_channel is None):
    duration_time = pretime_dict[before.name] - datetime.datetime.now()
    duration_time_adjust = int(duration_time.total_seconds()) * -1

    reply_channel_name = "general"
    reply_channel = [channel for channel in before.server.channels if channel.name == reply_channel_name][0]
    reply_text = after.name + "　が　"+ before.voice_channel.name + "　から抜けました。　通話時間：" + str(duration_time_adjust) +"秒"

    await client.send_message(reply_channel ,reply_text)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
