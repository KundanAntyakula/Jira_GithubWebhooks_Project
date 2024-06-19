from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__) #creating flask app instance

@app.route("/createJIRA", methods=['POST']) 

def createJIRA():
    
    url = "https://kundan-antyakula.atlassian.net/rest/api/3/issue"

    APITOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    auth = HTTPBasicAuth("kundanantyakula@gmail.com", APITOKEN)

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

        "summary": "first jira ticket",
        
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run('0.0.0.0',port=5000)
#to build we need server but flask has inbuilt development server without deploying on tomcat or bla bla