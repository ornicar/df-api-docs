import requests

url = "https://www.directfreight.com/api/postings/%7Bposting_type%7D"

querystring = {"posting_id":"SOME_ARRAY_VALUE"}

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

response = requests.request("DELETE", url, headers=headers, params=querystring)

print(response.text)