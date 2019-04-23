import requests
stad = input("vilken stad vill du se vädret i :\n>").lower() 
url ="https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/"+stad
r = requests.get(url)#gör en request från väder apin
response = r.json()#declarar vårat lib som response iställent för en Json 

print(response["city"])
for day in response["forecasts"]:
    print(day["date"],"    ",day["forecast"])#printar de väder som man ber om
