import requests
def get(url):
    response = requests.get(url)#hämtar data från url:en
    lib= response.json()#gör om datan till ett library
    return lib# ger tillbaka library