import requests

def getInfoAstronauti():
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()
    return data["people"]