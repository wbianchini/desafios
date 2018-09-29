import json
import requests
import urllib

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../code'))
from reddit_crawler import RedditCrawler

class NadaPraFazerBot:

	TOKEN = "628796129:AAHQIAJPSatKOt_GTfY3hnUnE12NzraeNUY"
	URL = "https://api.telegram.org/bot{}/".format(TOKEN)

	def get_from_url(self, url):
		response = requests.get(url)
		content = response.content.decode("utf8")
		return content

	def get_updates(self, offset=None):
		url = self.URL + "getUpdates?timeout=100"
		if offset:
			url +="&offset={}".format(offset)
		return self.get_json_from_url(url)

	def get_last_update_id(self, updates):
		update_ids = []
		for update in updates["result"]:
			update_ids.append(int(update["update_id"]))
		return max(update_ids)

	def get_json_from_url(self, url):
		content = self.get_from_url(url)
		return json.loads(content)

	def get_last_chat_id_and_text(self, updates):
		last_update = len(updates["result"]) -1
		text = updates["result"][last_update]["message"]["text"]
		chat_id = updates["result"][last_update]["message"]["chat"]["id"]
		return (text, chat_id)

	def send_message(self, text, chat_id):
		text = urllib.parse.quote_plus(text)
		url = self.URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
		self.get_from_url(url)

	def handle_updates(self, updates):
		for update in updates["result"]:
			try:

				message_text = update["message"]["text"]

				if message_text.startswith('/nadaprafazer') == False:
					raise Exception('Command not found')

				cmd = message_text.replace("/nadaprafazer ", "")
				crawler = RedditCrawler()

				if cmd:
					crawler.set_sub_reddits(cmd.strip())

				crawler.crawl()
				text = crawler.get_text_message()
				chat = update["message"]["chat"]["id"]
				
				self.send_message(text, chat)
			except Exception as e:
				print(e)
