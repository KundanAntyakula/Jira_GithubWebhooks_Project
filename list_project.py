import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://kundan-antyakula.atlassian.net/rest/api/3/project"


API_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

auth = HTTPBasicAuth("kundanantyakula@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}



response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
ouput = json.loads(response.text)
for i in ouput:
    print(i['name'])
