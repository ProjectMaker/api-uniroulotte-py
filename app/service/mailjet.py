import os
from mailjet_rest import Client

mailjet = Client(auth=(os.getenv('MAILJET_KEY_PUBLIC'), os.getenv('MAILJET_KEY_SECRET')), version='v3.1')


def get_message(to, firstname, lastname, price):
    return {
        'Messages': [{
            'From': {
                'Email': 'devis@uni-roulotte.fr',
                'Name': 'Uni-roulotte'
            },
            'To': [{
                'Email': to,
                'Name': f'{firstname} {lastname}'
            }
            ],
            'TemplateID': int(os.getenv('MAILJET_TEMPLATE_DEVIS')),
            'TemplateLanguage': True,
            'Subject': 'Votre devis',
            'Variables': {
                'PRICE': price
            }
        }]

    }


def send_message(to, firstname, lastname, price):
    result = mailjet.send.create(get_message(to, firstname, lastname, price))
    return {'status_code': result.status_code, 'data': result.json()}
