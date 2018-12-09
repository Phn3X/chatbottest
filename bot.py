import random
import re
import time
import facebook
from flask import Flask, request
from pymessenger.bot import Bot


app= Flask(__name__)
ACCESS_TOKEN= 'EAAcWiYBil7cBAAUBRABtSQ4zhsgj2mmy1EaMHBTeKuZA9t68yScxnsZAglKxXZCCNRMKIJQMbTkmzZAr9xQN1Sc4LgwWtl6MamJulB2MVCb0ssGe2ZCWJNl4M1iL8avnrpCQ3n90VbImy64oiE4bfMQmGZCPCVU00jz319ymGpxgZDZD'
VERIFY_TOKEN= '234q4qq545fqeq3'
bot= Bot(ACCESS_TOKEN)


@app.route('/', methods=['GET','POST'])


def receive_message():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return("incorrect verifciation token")
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
                replies = {"toast":["hi! Here's a lovely pina collada toast recipe for you! \n https://bit.ly/2BZYc4j" ],"fish":["Hi! Here's a lovely fish recipe for you! \n https://goo.gl/eopxdP"],"soup":["Hi! Here's a tasty corn soup recipe just for you! \n https://goo.gl/S4FcsE"],"pork":["Hi! Here's a pork recipe that's sure to taste divine! \n https://goo.gl/uGU8UR"]}

                for item in split:
                    if item in replies:
                        reply_text=random.choice(replies[item])
                        return(reply_text)



def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()
