import random

import utils
import cfg

from thrasher import Thrasher

""" class to send general data about an interaction to a command """
class ThrashCmd:
	cmd = ""
	tokens = []
	tokens_count = 0
	message = None
	client = None
	mentions = []
	mentions_count = 0

	def __init__(
		self,
		tokens = [],
		message = None,
		client = None,
		mentions = []
	):
		self.tokens = tokens
		self.message = message
		self.client = client
		self.mentions = mentions
		self.mentions_count = len(mentions)

		if len(tokens) >= 1:
			self.tokens_count = len(tokens)
			self.cmd = tokens[0]


async def link_image(cmd, booru_list):
	response = random.choice(booru_list)
	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def thrash(cmd):
	user_data = Thrasher(id_user=cmd.message.author.id)
	user_data.thrashcoin += 1
	user_data.persist()

	response = '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_rf + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + '\n' + cfg.emote_munchy + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_munchy + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf
	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def double_thrash(cmd):
	user_data = Thrasher(id_user = cmd.message.author.id)
	user_data.thrashcoin += 2
	user_data.persist()

	if user_data.thrashcoin >= 10:
		response = '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_rf + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + '\n' + cfg.emote_munchy + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_munchy + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf
		for i in range(2):
			await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))
		return

	else:
		response = "You don't have enough !thrashcoin to !doublethrash. ({}/10)".format(user_data.thrashcoin)

	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def triple_thrash(cmd):
	user_data = Thrasher(id_user = cmd.message.author.id)
	user_data.thrashcoin += 3
	user_data.persist()

	if user_data.thrashcoin >= 100:
		response = '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_rf + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + '\n' + cfg.emote_munchy + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_munchy + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf
		for i in range(3):
			await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))
		return

	else:
		response = "You don't have enough !thrashcoin to !triplethrash. ({}/100)".format(user_data.thrashcoin)

	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def quadruple_thrash(cmd):
	user_data = Thrasher(id_user = cmd.message.author.id)
	user_data.thrashcoin += 4
	user_data.persist()

	if user_data.thrashcoin >= 1000:
		response = '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_rf + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + '\n' + cfg.emote_munchy + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_munchy + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf
		for i in range(4):
			await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))
		return

	else:
		response = "You don't have enough !thrashcoin to !quadruplethrash. ({}/1000)".format(user_data.thrashcoin)

	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def quintuple_thrash(cmd):
	user_data = Thrasher(id_user = cmd.message.author.id)
	user_data.thrashcoin += 5
	user_data.persist()

	if user_data.thrashcoin >= 10000:
		response = '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_rf + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + '\n' + cfg.emote_munchy + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_munchy + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf
		for i in range(5):
			await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))
		return

	else:
		response = "You don't have enough !thrashcoin to !quintuplethrash. ({}/10000)".format(user_data.thrashcoin)

	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def sextuple_thrash(cmd):
	user_data = Thrasher(id_user = cmd.message.author.id)
	user_data.thrashcoin += 6
	user_data.persist()

	if user_data.thrashcoin >= 100000:
		response = '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_rf + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + '\n' + cfg.emote_munchy + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_munchy + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf
		for i in range(6):
			await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))
		return

	else:
		response = "You don't have enough !thrashcoin to !sextuplethrash. ({}/100000)".format(user_data.thrashcoin)

	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def septuple_thrash(cmd):
	user_data = Thrasher(id_user = cmd.message.author.id)
	user_data.thrashcoin += 7
	user_data.persist()

	if user_data.thrashcoin >= 1000000:
		response = '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_rf + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + '\n' + cfg.emote_munchy + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_s1 + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_munchy + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s3 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + '\n' + cfg.emote_blank + cfg.emote_blank + cfg.emote_blank + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_s1 + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf + cfg.emote_rf
		for i in range(7):
			await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))
		return

	else:
		response = "You don't have enough !thrashcoin to !septuplethrash. ({}/1000000)".format(user_data.thrashcoin)

	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def takedown(cmd):
	response = "https://cdn.discordapp.com/attachments/522236656086941736/638174609719427090/mathew-thumbs-down.gif"
	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def themes(cmd):
	response = 'https://www.youtube.com/playlist?list=PL_Lh9cF2MSf1AeTsszptxrupK0Zds6S5G'
	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def gamering(cmd):
	response = 'https://youtu.be/jdtstiuYxis'
	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def frog(cmd):
	response = 'Who?'
	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def goodboy(cmd):
	response = "https://img.booru.org/rfck//images/1/93c3572a5ae571efe866620cc0c744147d597c24.jpg"
	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def laughtrack(cmd):
	response = cfg.emote_etlaugh
	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def modelo(cmd):
	response = "https://youtube.com/watch?v=Gd9P378edq4"
	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def vibecheck(cmd):
	response = "Vibe checking is currently under construction."
	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def miller(cmd):
	response = "Who? (use !milly)"
	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def kanman(cmd):
	response = "Who? (use !kanny)"
	return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def thrashcoin(cmd):
	if cmd.mentions_count == 0:
		user_data = Thrasher(id_user = cmd.message.author.id)

		response = "You currently have {} !thrashcoin.".format(user_data.thrashcoin)
		return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

	else:
		user_data = Thrasher(id_user = cmd.mentions[0].id)

		response = "They currently have {} !thrashcoin.".format(user_data.thrashcoin)
		return await utils.send_message(cmd.client, cmd.message.channel, utils.formatMessage(cmd.message.author, response))

async def leaderboard(cmd):
	response = "{rf} ▓▓▓▓▓ TOP THRASHERS ▓▓▓▓▓ {rf}\n".format(
		rf = cfg.emote_rf
	)


	conn_info = utils.databaseConnect()
	conn = conn_info.get('conn')
	cursor = conn.cursor()

	cursor.execute(
			"SELECT t.id_user, t.thrashcoin " +
			"FROM thrashers as t " +
			"ORDER BY t.thrashcoin DESC LIMIT 10"
	)

	data = cursor.fetchall()
	if data != None:
		for row in data:
			if cmd.message.guild.get_member(int(row[0])) is not None:
				response += "{} `{:_>15} | {}`\n".format(
					cfg.emote_blank,
					row[1],
					cmd.message.guild.get_member(int(row[0])).display_name.replace("`", ""),
				)

	# Clean up the database handles.
	cursor.close()
	utils.databaseClose(conn_info)

	return await utils.send_message(cmd.client, cmd.message.channel, response.replace("@", "\{at\}"))
