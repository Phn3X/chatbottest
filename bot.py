import random
import re
import time
import facebook
from flask import Flask, request
from pymessenger.bot import Bot


app= Flask(__name__)
ACCESS_TOKEN= 'EAAC6SbRKAIcBAB8D01ugZBdATy27fbfeVmH3YR6AzZAg1lAZChCJRvLr32eXhk3iG3FDwYriIUmwSRWNkhKmWylGndf5wPpwWHRbWFIhZCtevXNbrakDiwb2C9ZATluxi9cBPMOWkR29L26ouREhhakNIHIjm2xV2vFbU1lUcRwZDZD'
VERIFY_TOKEN= 'qsqweu1234u103idfn0nr34nr1024r5913j0f30'
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
                replies = {"hiring":["Hello, we are always accepting applications as job opportunities can come up at any time. We require that you are able to read and write, and that you obtain a certificate of good character. Bring the certificate and a printed photo of yourself to any branch where you can ask for the application form, fill it out, and leave it with the manager. Any references (if you have food prep/restaurant/other experience) can be included on the form. If you find it difficult to print a photo of yourself it is not absolutely required, but generally better to include. Looking forward to getting your application!"],
                "vacancy":["Hello, we are always accepting applications as job opportunities can come up at any time. We require that you are able to read and write, and that you obtain a certificate of good character. Bring the certificate and a printed photo of yourself to any branch where you can ask for the application form, fill it out, and leave it with the manager. Any references (if you have food prep/restaurant/other experience) can be included on the form. If you find it difficult to print a photo of yourself it is not absolutely required, but generally better to include. Looking forward to getting your application!"],
                "vacancies":["Hello, we are always accepting applications as job opportunities can come up at any time. We require that you are able to read and write, and that you obtain a certificate of good character. Bring the certificate and a printed photo of yourself to any branch where you can ask for the application form, fill it out, and leave it with the manager. Any references (if you have food prep/restaurant/other experience) can be included on the form. If you find it difficult to print a photo of yourself it is not absolutely required, but generally better to include. Looking forward to getting your application!"],
               "located":["we have branches located at Ariapita Avenue, Diego Martin, Fernandes Compound, Barataria and Port of Spain"],"hours":["The Ariapita Avenue branch opens from  10 am to 9pm Monday to Thursday, 10am to 9:30 pm Friday and Saturday and 9am to 3:30pm on Sunday. The Diego Martin branch opens from 10am to 8pm Monday to Saturday and 9am to 3:30pm on Sunday. The Barataria branch opens from 10am to 4pm Monday to Sunday. The branch at Fernandes Compound opens from 10am to 4pm Monday to Saturday and our new Park Street Port of Spain branch opens from 10am to 5pm Monday to Saturday"],"halal":["All our meats are Halal!"]}


                replies1 = {"when does the ariapita branch open":["The ariapita avenue branch opens from  10 am to 9pm Monday to Thursday, 10am to 9:30 pm Friday and Saturday and 9am to 3:30pm on Sunday."],"when does the diego martin branch open":["The Diego Martin branch opens from The Diego Martin branch opens from 10am to 8pm Monday to Saturday and 9am to 3:30pm on Sunday."],
                "when does the barataria branch open":["The Barataria branch opens from 10am to 4pm Monday to Sunday."],"when does the branch at fernandes compound open":["The branch at fernandes compound opens from 10am to 4pm Monday to Saturday"],"when does the park street branch open":["The branch at Park Street is open from 10am to 5pm Monday to Saturday"]}
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
