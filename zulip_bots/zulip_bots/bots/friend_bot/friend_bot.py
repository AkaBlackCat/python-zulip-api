import requests
import logging
import zulip

class FriendBotHandler(object):
	'''
	A docstring documenting this bot.
	'''

	def usage(self):
		return '''Your description of the bot'''

	def handle_message(self, message, bot_handler):
		original_content = message['content']
		original_sender = message['sender_email']
		new_content = original_content.replace('@followup','from %s:' % (original_sender,))

	bot_handler.send_message(dict(
		type='private', # can be 'stream' or 'private'
		to='followup', # either the stream name or user's email
		subject=message['sender_email'], # message subject
		content=message['content'], # content of the sent message
	))

	response = "Dont worry, Im here for you buddy :pepelove:"

	if "friend" in message:
		bot_handler.send_reply(message, response)


handler_class = FriendBotHandler
