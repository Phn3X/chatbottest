import random
import re
import time
import facebook
from flask import Flask, request
from pymessenger.bot import Bot


app= Flask(__name__)
ACCESS_TOKEN= 'EAAFxSZCHMvkEBAJbWz7FYejFZAOtUDAv3AJfLmBBoHUI4v2fgWGriznSPrFGXDZASuq2jFQU7W5Jv1KNfb6PDJH5fXIb62snu6ZCGCyf0SRZBpT8FcYrwAnCVhTXpo6SJLotOGhOJKMxoymfvJSffBFQAvkr0cxPuUSGCCRAVygZDZD'
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

def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verifcation token'

def get_message():

    output = request.get_json()
    for event in output['entry']:
        messaging = event['messaging']
        for message in messaging:
            if message.get('message'):
                split = re.sub(r"[^a-zA-Z0-9\s]",' ',message['message'].get('text')).lower().split()
                replies = {"hi":["hello! and welcome to bad rabbit! how can I help you?"],
                "services":["we offer writing services, content ideation and app development! "],"opening hours":["we're open 24/7 so feel free to drop a line!"]}


                for item in split:
                    if item in replies:
                        reply_text=random.choice(replies[item])
                        print(split)
                        time.sleep(5)
                        return(reply_text)
                    elif item in replies1:
                        reply_text1=random.choice(replies1[item])
                        return(reply_text1)


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"


if __name__ == "__main__":
    app.run()
