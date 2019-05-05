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
                user_id = message['sender']['id']
                if message['message'].get('text'):
                    response_sent_text = get_message()
                    send_message(user_id, response_sent_text)
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(user_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    else:
        return "wrong token"


def get_message():
    sample_responses = ["Zdravo","Milo mi e shto ne dodadovte","Kako ste denes?","Izgledate odlicno"]
    return random.choice(sample_responses)

def send_message(user_id, response):
    bot.send_text_message(user_id, response)
    return "success"
#Defining url
URLSelectUser= "http://viberapi.inellipse.com/api/select-users/"
URLAddUser= "http://viberapi.inellipse.com/api/add-users"
URLSelectPlates= "http://viberapi.inellipse.com/api/select-plates/"
URLAddPlates= "http://viberapi.inellipse.com/api/add-plates/"
URLAddMsg="http://viberapi.inellipse.com/api/add-messages/"

def AddUser(ACCESS_TOKEN,user_id,message_data,dateCreated=('Y-m-d H:i:s')) #Post request for adding a user

header = {
    'Content-Type':'application/json'
}
params = {
    'access_token'= ACCESS_TOKEN
}
payload = {
    'recipient':{
        'id'=user_id
    }
    'message'=message_data
    'CreationDate'=dateCreated
}
url=URLAddUser
response = request.post(url,header,params=params,data=json.dumps(payload))
response.raise_for_status()
return response.json()
print("User succesfully added")

def AddPlates(ACCESS_TOKEN,plate_numbers,user_id,dateCreated=('Y-m-d H:i:s')); #Post requst for adding plates
headerA = {
    'Content-Type':'application/json'
}
paramsA = {
    'access_token'=ACCESS_TOKEN
}
payloadA = {
    'Numberplate'=plate_numbers
    'id'=user_id
    'DateCreated'=dateCreated
}
urlA=URLAddPlates
responseA= request.post(urlA,headerA,params=paramsA,data=json.dumps(payloadA))
return responsA.json()
print("You have sucessfully added your plate number")

def AddMessage(ACCESS_TOKEN,get_message); #post request for adding messages
headerB = {
    'Content-Type':'application/json'
}
paramsB={
    'access_token'=ACCESS_TOKEN
}
payloadB={
    'Messages'=get_message()
}
urlB=URLAddMsg
responseB= request.post(urlB,headerB,params=paramsB,data=json.dumps(payloadB))
return responseB.json()
print("Your message is stored.")

if __name__ == "__main__":
    app.run()
