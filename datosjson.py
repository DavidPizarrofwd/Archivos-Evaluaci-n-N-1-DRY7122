import json

with open ('myfile.json', 'r') as json_file:
    ourjson = json.load(json_file)

token = ourjson['access_token']
tiempo_restante = ourjson['expires_in']

print("El valor del token es: " + token)
print ("El tiempo restante antes de que caduque es: " + str(tiempo_restante) + " segundo.")