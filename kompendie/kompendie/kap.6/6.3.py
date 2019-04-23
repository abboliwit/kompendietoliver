import requests
url1 = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
r = requests.get(url1)
response = r.json()
print("Artsit DB")
for artist in response["artists"]:#printar alla artister
    print(artist["name"])

select = input("Select artist:\n >").capitalize()# tar in vilket artist du vill ha

for artist in response["artists"]:
    if artist["name"] == select:
        Id = artist["id"]
        break

url2 = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"+Id#tar det nya värdet
u = requests.get(url2)
Response = u.json()
Data = ""
Data += Response["artist"]["name"] + "\nGenres" + str(Response["artist"]["genres"])  + "\nYears Active" + str(Response["artist"]["years_active"])# gör en string av alla värden
print(Data)# printar ut allt




    
