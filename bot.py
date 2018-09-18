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
                replies = {"menu":["Hi! Thanks for getting in touch. Please click here to see our Menu: http://bit.ly/2r02sf0"],"hours":["Hello, thanks for getting in touch! Our Kaizan Port-Of-Spain branch is located at Shop #15, MovieTowne, POS. For reservations or more information please give us a call at 623-5437 or 222-4441. Our Kaizan Chaguanas branch is located at Shop #12A North, Price Plaza. For reservations or more information please give us a call at 672-1815, 672-6601 or 221-8983." /n"Our opening hours for this location are as follows: Sun - Thur 11.00am – 10.30pm Fri - Sat 11.00am – 11.00pm Kind regards, The Kaizan Team "],"contact":["Hello , thanks for getting in touch! Our Kaizan Port-Of-Spain branch is located at Shop #15, MovieTowne, POS. For reservations or more information please give us a call at 623-5437 or 222-4441. /nOur Kaizan Chaguanas branch is located at Shop #12A North, Price Plaza. For reservations or more information please give us a call at 672-1815, 672-6601 or 221-8983. Our opening hours for this location are as follows: Sun - Thur 11.00am – 10.30pm Fri - Sat 11.00am – 11.00pm Kind regards The Kaizan Team"],"do you deliver?":["Hi Jake , Please see the delivery menu here: http://bit.ly/Kaizansushi Here are the numbers to call to place your order: Price Plaza Chaguanas 672-1815, 672-6601 or 221-8983. MovieTowne POS: 623-5437 & 222-4441 You can also order via our app which is available for Android and iOS. For MovieTowne Port-of-Spain we deliver to Port-of-Spain and environs, Diego Martin as far as Blue Range and Maraval as far as Moka. For Price Plaza we deliver to: Lange Park and similar distance East of the highway,  Orchards Gardens or similar distance west of the highway and  Anything further out as far as Edinburgh 500."],"thank":["You're most welcome! We hope to hear from you again!"],"thanks":["You're most welcome! We hope to hear from you again!"]}
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
