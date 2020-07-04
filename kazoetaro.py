import discord
import datetime
import time
from config_parser import ConfigParser
from functools import wraps

import os
import subprocess
import logging
import traceback
import sys

client = discord.Client()
pretime_dict = {}


class Kazoetaro():
	def __init__(self):
		pass

	def setNotifyChannel(self, channel="kazoetaro"):
		print("setNotifyChannel is called")
		self.channel = channel

	@client.event
	async def on_ready():
		print("on_ready")
		pass

	@client.event
	async def on_message(message):
		print('Message from {0.author}: {0.content}'.format(message))

	@client.event
	async def on_voice_state_update(member, before, after):
		# bot かどうかチェック
		if member.bot:
			print("I'm BOT")
			return
		print("I'm NOT BOT")
		guild = member.guild
		reply_to_chName = "kazoetaro"
		reply_to_chId = None

		for channel in guild.text_channels:
			if channel.name == reply_to_chName:
				reply_to_chId = channel.id

		channel = client.get_channel(reply_to_chId)

		# 入室時
		if (before.channel is None):
			pretime_dict[member.display_name] = datetime.datetime.now()
			print(pretime_dict[member.display_name])
			reply_message = "「"+member.display_name + "」がVCに入ったで。今から時間測ったる"
			await channel.send(reply_message)

		# 退出時
		if (after.channel is None):
			print(pretime_dict[member.display_name])
			duration_time = pretime_dict[member.display_name] - datetime.datetime.now()

			try:
					execution_time = int(duration_time.total_seconds()) * -1
					print(execution_time)
					if  execution_time <60 :
							reply_message = "「" + member.display_name +  \
								"」がVCから出ていったで。時間は…" +str(execution_time)+ \
								"秒か…やる気ある??"
							await channel.send(reply_message)
					
					elif 60 <= execution_time < 3600:
							# minutes
							h,m, s = get_h_m_s(execution_time)
							reply_message = "「" + member.display_name +  \
							"」がVCから出ていったで。時間は…" +\
							str(m) + "分" + str(s) + "秒やな…ええんちゃうん？"

							await channel.send(reply_message)

					elif 3600 <= execution_time :
							# hour
							h, m, s = get_h_m_s(execution_time)
							reply_message = "「"+ member.display_name +  \
							"」がVCから出ていったで。時間は…" +\
							str(h)+"時間"+str(m) + "分" + str(s) + "秒やな…やるやないか"
							await channel.send(reply_message)

			except Exception as e:
					tb = sys.exc_info()[2]
					print(sys.exc_info())
					print("Message:{0}".format(e.with_traceback(tb)))
					print("Trace:{0}".format(e.with_traceback(sys.exc_info())))

					await channel.send("なーんかエラー起きたみたいやで...すまんな")


def get_h_m_s(td):
	m, s = divmod(td, 60)
	h, m = divmod(m, 60)
	return h, m, s


if __name__ == "__main__":
	APIKEY=None
	try: 
		# parser = ConfigParser()
		# config = parser.load()
		# APIKEY = config.get('bot', 'APIKEY')
		pass
	except: 
		pass

	# kazoetaro = Kazoetaro()
	# kazoetaro.setNotifyChannel()


	if APIKEY is None:
		APIKEY=os.environ['APIKEY']

		print("APIKEY:", APIKEY)

	client.run(APIKEY)
