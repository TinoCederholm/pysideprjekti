import requests

API_OSOITE = "https://opentdb.com/api.php?amount=10"

def lataa_kysymykset_netista():
    vastaus = requests.get(API_OSOITE)
    tiedot = vastaus.json()
    for juttu in tiedot ["results"]:
    print(tiedot)
    
if __name__ == "__main__":
    lataa_kysymykset_netista()


