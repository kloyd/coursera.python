import urllib.request, urllib.parse, urllib.error
import json

data = '''
{
    "users": [
        {
            "status": {
                "text": "@jazzychad I just bought one .__."
             },
             "location" : "San Francisco, California",
             "screen_name" : "leahculver",
             "name": "Leah Culver"
         },
        {
            "status": {
                "text": "@jazzychad I just bought one .__."
             },
             "location": "San Francisco, California",
             "screen_name": "leahculver",
             "name": "Leah Culver"
         }
    ]
}'''

x = json.loads(data)
print(x['users'][0]['name'])
