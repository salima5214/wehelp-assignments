import json
import urllib.request, json

with urllib.request.urlopen("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json") as url:
    data = json.loads(url.read().decode("utf-8"))

with open("data.csv","w",encoding="utf-8",newline="") as csvfile:
    for i in range(len(data["result"]["results"])):
        csvfile.write(data["result"]["results"][i]["stitle"]+","+data["result"]["results"][i]["address"][5:8]+","+data["result"]["results"][i]["longitude"]+","+data["result"]["results"][i]["latitude"]+","+"https://"+data["result"]["results"][i]["file"].split("https://")[1]+"\n")
