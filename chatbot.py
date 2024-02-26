from flask import Flask, request, jsonify
from flask_cors import CORS
from twilio.rest import Client
from module import chatbot

app = Flask(__name__)
CORS(app)

account_sid = 'AC1fd791b5315914ad9eff0fcc80a30077'
auth_token = '5af9187a8311e2342dada61b99d0fd8d'
whatsapp_number = 'whatsapp:+14342645789'

client = Client(account_sid, auth_token)

port = 5003

@app.route('/')
def hello():
    print("----***Hello World***---")
    return "----***Hello World***---"

# chatbot message start
@app.route('/ai/answer', methods=['GET', 'POST'])
def answer():
    if request.method == 'POST':
        try:
            data = request.get_json()  # Get the JSON data from the request
            tempData = data['request']
            print(tempData)
            if not tempData:
                tempData = "Empty Data"
            print("request_data", tempData)
            response = chatbot(tempData)
            print("print_response", response)
            return jsonify({'response': response})
        except:
            return jsonify({'message': 'Invalid JSON payload.'}), 400  # Return a 400 Bad Request response for invalid JSON
    else:
        response = {'message': 'Please provide a name.'}
        return jsonify(response)
# chatbot message end

# whatsapp message send start
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message_body = data['Body']
    print(message_body)
    sender_number = data['From']
    
    # Process the message as needed
    response_message = chatbot(message_body)
    # Send a response message    
    message = client.messages.create(
        body=response_message,
        from_= whatsapp_number,  # Your Twilio sandbox number or your WhatsApp-enabled number
        to= sender_number
    )
    
    return '', 200


if __name__ == '__main__':
    print("Server is running on", port)
    from waitress import serve
    # app.run(port=port)
    # serve(app, host='192.168.146.239', port=port)
    serve(app, port=port)