#enviar msg p celular via twilio
# para cadastrar numero: www.twilio.com/try-twilio
from twilio.rest import TwilioRestClient

account_sid = "ACDLKSDAA234234JN234"
auth_token = "fasd12387ksadskj"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body = "My name is Teste",
    to="+165473829",     #mudar seu numero
    from_="+165473829")  #mudar com o numero twilio

print message.sid
