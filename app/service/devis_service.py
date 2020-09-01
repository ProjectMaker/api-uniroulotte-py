from service.mailjet import send_message
from model.devis_model import Devis

class DevisService(object):
    @staticmethod
    def create(**payload):
        devis = Devis(**payload)
        devis.save()
        send_message(payload['email'], payload['firstname'], payload['lastname'], payload['price'])
