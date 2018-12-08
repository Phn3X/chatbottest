import random
import re
import time
import facebook
from flask import Flask, request
from pymessenger.bot import Bot


app= Flask(__name__)
ACCESS_TOKEN= 'EAAFxSZCHMvkEBAJ9D6KAYpkOELNZBfzxweLZAgAfoI0yYDrNeEVoU2pbXnvEydjgmVI915JmDqgyWR8uk98EWifYZAeZB7zX8mVkFmLYmjT9dCuVA1bIUcmpMCckew7eE7VeDZBlUQgZAbwctZCwur8QxmvLnynGZAPZAdrjDN4Ske2AZDZD'
VERIFY_TOKEN= '1123qwe13qdwrq3452435'
bot= Bot(ACCESS_TOKEN)


@app.route('/', methods=['GET','POST'])


def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_text)
                    if message['message'].get('attachments'):
                        response_sent_nontext = get_message()
                        send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def get_message():

    output = request.get_json()
    for event in output['entry']:
        messaging = event['messaging']
        for message in messaging:
            if message.get('message'):
                split = re.sub(r"[^a-zA-Z0-9\s]",' ',message['message'].get('text')).lower().split()
                replies = {"toast":"1.jpg"}

                for item in split:
                    if item in replies:
                        reply_text=random.choice(replies[item])
                        print(split)
                        return(reply_text)

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()
