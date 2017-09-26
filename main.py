from fbchat import Client, log
import twilio.rest
from getpass import getpass

to="+917376335104"					# Your mobile number assosiated to twilio on which you'll get messages
from_="+1415******"					# Twilio number
SID = "ACed16c3e*************"		# Twilio Sid number
Tocken = "dbb7c5f5b**********"		# Twilio tocken number

username = str(raw_input("Facebook_Username: "))  	# For facebook username
password = getpass()								# For Facebook password

# for sending the Message
def sendMessage(SID, Tocken, to ,from_ ,body):
	client = twilio.rest.Client(SID, Tocken)
	client.messages.create(to= to, from_ = from_, body= body)

class EchoBot(Client):
    def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
    	# If you're sending message to someone on fb then it will not gonna send a message to you on phone
        if author_id != self.uid:
		
		user = client.fetchUserInfo(author_id)[author_id]
		Sender = user.name

		body = ":\nMessage from " + Sender + "\nmessage is - " + message
		sendMessage(SID, Tocken, to ,from_ , body)
		
		print "Message send on your mobile number"

client = EchoBot(username, password)
client.listen()