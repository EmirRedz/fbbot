import random
from flask import Flask, request
from pymessenger.bot import Bot
import requests



app = Flask(__name__)
ACCESS_TOKEN = 'EAAfDeGr0WnkBAIRFG557JhKbDZAvhthFjry4xO0K4Tfq129X7sIMG7uqdLOT4znP5CH7WTmkbB4LZBAsKKvO1utHxhOwxbJLDKtvEIhaiBqmCAUlfhCz7cFrGBsAVxDcbJmT58YSs8MA3JkgdHGM5v8bbSYBlVEMWFCujg34IhJOUgx7cP'
VERIFY_TOKEN = 'testing12345'
bot = Bot(ACCESS_TOKEN)

@app.route("/", methods=['GET', 'POST'])
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
    else:
        return "wrong token"


def get_message():
    sample_responses = ["Zdravo","Milo mi e shto ne dodadovte","Kako ste denes?","Izgledate odlicno"]
    return random.choice(sample_responses)

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"



if __name__ == "__main__":
    app.run()