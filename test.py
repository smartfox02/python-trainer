from flask import Flask, request, jsonify
from flask_cors import CORS
from module import chatbot
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)
CORS(app)
from twilio.rest import Client
port = 5004
account_sid = 'AC1fd791b5315914ad9eff0fcc80a30077'
auth_token = '5af9187a8311e2342dada61b99d0fd8d'
whatsapp_number = 'whatsapp:+14342645789'

client = Client(account_sid, auth_token)

@app.route('/')
def hello():
    print("----***Hello World***---")
    return "----***Hello World***---"

# ngrok message test start
@app.route('/sms', methods=['POST'])
def receive_sms():
    print("request:", request)
    data = request.form
    message_body = data['Body']
    print("message_body:", message_body)  # Output: <class 'str'>
    
    # Process the message as needed
    response_message = chatbot(message_body)
    # Send a response message
    message = client.messages.create(
        body=response_message,
        from_= whatsapp_number,  # Your Twilio sandbox number or your WhatsApp-enabled number
        to= 'whatsapp:+18105458584'
    )
    print(message);
    response = MessagingResponse()
    response.message(response_message)
    return str(response)


# ngrok message test end

if __name__ == '__main__':
    print("Server is running on", port)
    from waitress import serve
    # app.run(host='localhost', port=port)
    serve(app, host='localhost', port=port)