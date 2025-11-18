 
import os
import re
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    
    # Anti-link logic
    if re.search(r'http[s]?://|www\.|t\.me|bit\.ly', incoming_msg, re.IGNORECASE):
        resp.message("⚠️ *LINK DELETED!* Links are not allowed here.")
    else:
        resp.message("✅ Message approved!")  # Optional response
    
    return str(resp)

if __name__ == '__main__':
    app.run(port=5000)
