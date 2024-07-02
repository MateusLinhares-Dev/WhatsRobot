from flask import Flask, request
import requests
import json
import re
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_webhook():
    # Extrair dados da mensagem recebida
    response = MessagingResponse()

    message_body = request.form.get('Body')

    pattern = r"\nworkflow_title: (\d+)"
    match = re.search(pattern, message_body)

    if match:
        workflow_title = match.group(1).strip()

        workflow_instance = create_workflow(workflow_title)
        response.message("Workflow criado com sucesso! ID: {}".format(workflow_instance.id))

        return str(response)
    else:
        response.message("Mensagem template inválido, revise sua mensagem!")

def create_workflow(workflow_title):
    # Criar workflow
    workflow_formatted = workflow_title
    __url_sesuite = 'https://isc.softexpert.com/apigateway/se/exp/chatbot/api/instance.php?'
    __header = {'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MDk3NTMyNDIsImV4cCI6MTc2NzIyNTU0MCwiaWRsb2dpbiI6Im1hdGV1cy5saW5oYXJlcyIsInJhdGVsaW1pdCI6MTIwLCJxdW90YWxpbWl0IjoxMDAwMDB9.JlBd2kreOy8ArX1M-QLobAQaIdPBmZvUSEndKa61Qxo'}
    __data = f'idProcess=AE001&cdProduct=39&nmInstance={workflow_formatted}'
    __url_data = f'{__url_sesuite}{__data}'
    __response = requests.post(__url_data, headers=__header)

    return __response

if __name__ == "__main__":
    app.run()

