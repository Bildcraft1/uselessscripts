from telethon import TelegramClient, events
import os
import keep_alive

keep_alive.keep_alive()

api_id = os.environ["api_id"]
api_hash = os.environ["api_hash"]
client = TelegramClient("anon", api_id, api_hash)
chat_id = os.environ["chat_id"]


@client.on(events.NewMessage(chats=chat_id))
async def logger(event):
    sender = await event.get_sender()
    if event.message.text and not event.message.media:
        print("{}: {}".format(sender.first_name, event.message.text))
    else:
        print("{}: *sent a media*".format(sender.first_name))


client.start()
print("Connected")
client.run_until_disconnected()
