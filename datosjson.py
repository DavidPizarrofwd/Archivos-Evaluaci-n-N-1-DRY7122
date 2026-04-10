import json

with open ('myfile.json', 'r') as jsonnEV:
    DAJOjson = json.load(jsonnEV)

token = DAJOjson['access_token']
expirar_tiempo = DAJOjson['expires_in']

print("El valor del token es: " + token)
print ("El tiempo para que caduque es: " + str(expirar_tiempo) + " segundo.")