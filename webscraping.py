import requests
url = 'https://api.github.com/users/TamaraBadik/events'
headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)
print(f"Status code: {response.status_code}")
# speichert die API Antwort in einer Variablen
json_response = response.json()
#verarbeitet die Ergebnisse .

# for single_item in array:
for github_event in json_response:
    if github_event['type'] == "PushEvent":
        print("###########")
        print(github_event['type'])
