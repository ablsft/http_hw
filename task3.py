import requests

url = 'https://api.stackexchange.com/2.3/questions'

params = {
    "fromdate": "1685923200",
    "todate": "1686096000",
    "order": "desc",
    "sort": "activity",
    "tagged": "Python",
    "site": "stackoverflow"
}

resp = requests.get(url, params=params)

for id, item in enumerate(resp.json().get("items")):
    print(f'{id+1}. {item["title"]}')
    print(item["link"] + "\n")