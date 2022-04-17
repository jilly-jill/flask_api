import json
import requests
from pprint import pprint

URL= "http://127.0.0.1:2224/data"


mutant ={"alias": "Emma Frost",
    "image": "https://vignette.wikia.nocookie.net/marveldatabase/images/d/d6/Emma_Frost_(Earth-616)_from_House_of_X_Vol_1_3_001.jpg/revision/latest/top-crop/width/720/height/900?cb=20190827212435",         
    "name": "Emma Frost",
    "location": "Krakoa",
    "powers": ["Telepathy", "Shapeshifting", "Telepathic Persuasion"],
    "quotes": [
        "Of course I'm a threat. Why? Did you think for a moment that I wasn't?",
        "The games are immaterial. What matters are the stakes."]
}

mutant= json.dumps(mutant)
# requests.post requires two arguments at the minimum;
# a url to send the request
# and a json string to attach to the request
resp = requests.post(URL, json=mutant)
# pretty-print the response back from our POST request
pprint(resp.json())


