import requests

url = "https://www.directfreight.com/api/profiles/documents"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'end-user-token': "SOME_STRING_VALUE"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)