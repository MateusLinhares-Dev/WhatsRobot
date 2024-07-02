from flask import Flask, request, jsonify
import json
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_webhook():
    # Extrair dados da mensagem recebida
    message_body = request.form.get('Body')
    from_number = request.form.get('From')

    # Responder com uma mensagem automática (opcional)
    response = MessagingResponse()
    response.message("Recebi sua mensagem: {}".format(message_body))

    return str(response)

if __name__ == "__main__":
    app.run()
