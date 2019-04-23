import requests
nummer = input("välj ett nummer ")
url = "http://77.238.56.27/examples/numinfo/?integer="+nummer
r = requests.get(url)
response = r.json()
if response["even"] == True:
    print("Even")
if response["prime"] == True:
    print("numret är ett primtal")
print ("factorer:"+str(response["factors"]))