import json

with open ('myfile.json', 'r') as jsonnEV:
    ourjson = json.load(jsonnEV)

token = ourjson['access_token']
expirar_tiempo = ourjson['expires_in']

print("El valor del token es: " + token)
print ("El tiempo para que caduque es: " + str(expirar_tiempo) + " segundo.")