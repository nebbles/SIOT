from requests import get
import json
from pprint import pprint


def call_dark_sky(key):
    # dbde = ("51.497999", "-0.174511") # Dyson Building
    london = ("51.506321", "-0.12714") # Lat, Long for London
    dsky = "https://api.darksky.net/forecast/{}/{loc[0]:},{loc[1]:}?exclude=minutely,hourly,daily&units=si".format(key, loc=london)
    resp = get(dsky)
    return json.loads(resp.text)


if __name__ == "__main__":

    with open('data_collection/credentials.json') as key_file:
        creds = json.load(key_file)
    
    data = call_dark_sky(creds['dark_sky'])
    pprint(data)
