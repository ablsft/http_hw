import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url)
compare_list = ['Hulk', 'Captain America', 'Thanos']
intelligence_dict = {}

for superhero in resp.json():
    if superhero['name'] in compare_list:
        intelligence_dict[superhero['name']] = superhero['powerstats']['intelligence']

most_intelligent = max(intelligence_dict, key=lambda x: intelligence_dict[x])

print(f'The most intelligent superhero from the chosen group ({", ".join(compare_list)}) is {most_intelligent}')
print(f'His intelligence score is {intelligence_dict[most_intelligent]}')