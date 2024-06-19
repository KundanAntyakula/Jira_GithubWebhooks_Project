import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://kundan-antyakula.atlassian.net/rest/api/3/issue"

APITOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth = HTTPBasicAuth("kundanantyakula@gmail.com", APITOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Order entry fails when selecting supplier.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
   
    "issuetype": {
      "id": "10006"
    },

    "project": {
      "key": "KUN"
    },

    "summary": "second jira ticket",
    
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
