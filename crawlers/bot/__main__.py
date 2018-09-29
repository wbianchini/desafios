import time
from nadaprafazerbot import NadaPraFazerBot

bot = NadaPraFazerBot();

last_update_id = None
while True:
	updates = bot.get_updates(last_update_id)
	if len(updates["result"]) > 0:
		last_update_id = bot.get_last_update_id(updates) + 1
		bot.handle_updates(updates)
	time.sleep(0.5)
