import web
lib = web.get("https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/stockholm")# andvänder modulen web för att hämta väder library frå API:n
print(lib)