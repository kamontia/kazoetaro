import discord
import datetime
import time
from config_parser import ConfigParser
from functools import wraps

import os
import subprocess

client = discord.Client()
pretime_dict = {}


class Kazoetaro():
	def __init__(self):
		pass

	def setNotifyChannel(self, channel="kazoetaro"):
		print("setNotifyChannel is called")
		self.channel = channel

	@client.event
	async def on_ready(self):
		print("on_ready")
		pass

	@client.event
	async def on_message(self, message):
		print('Message from {0.author}: {0.content}'.format(message))

	@client.event
	async def on_voice_state_update(self,member, before, after):
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
			reply_message = member.display_name + \
					"がVCから出ていったで。時間は…" +\
					str(execution_time) + "秒…こんなもんやろ"
			await channel.send(reply_message)

			# try:
			#     execution_time = int(duration_time.total_seconds()) * -1
			#     if execution_time >= 60:
			#         # minutes
			#         h, m, s = get_h_m_s(execution_time)
			#     elif execution_time >= 3600:
			#         # hour
			#         h, m, s = get_h_m_s(execution_time)

			#     print(execution_time)
			#     reply_message = member.display_name + \
			#         "がVCから出ていったで。時間は…" +\
			#         str(execution_time) + "秒…こんなもんやろ"
			#     await channel.send(reply_message)
			# except Exception:
			#     await channel.send("なーんかエラー起きたみたいやで...すまんな")


def stop_watch(func):
	@wraps(func)
	def wrapper(*args, **kargs):
		start = time.time()
		result = func(*args, **kargs)
		elapsed_time = time.time() - start
		return result, elapsed_time
	return wrapper


def get_h_m_s(td):
	m, s = divmod(td.seconds, 60)
	h, m = divmod(m, 60)
	return h, m, s


def measure_time():
	while True:
		pass


if __name__ == "__main__":
<<<<<<< HEAD
	APIKEY=None
	try: 
		parser = ConfigParser()
		config = parser.load()
		APIKEY = config.get('bot', 'APIKEY')
	except: 
		pass
=======
	parser = ConfigParser()
	config = parser.load()
>>>>>>> 58cc5fe... Add config parser

	kazoetaro = Kazoetaro()
	kazoetaro.setNotifyChannel()

<<<<<<< HEAD
=======
	APIKEY = config.get('bot', 'APIKEY')
>>>>>>> 58cc5fe... Add config parser

	if APIKEY is None:
		APIKEY=os.environ['APIKEY']

		print("APIKEY:", APIKEY)

	client.run(APIKEY)
