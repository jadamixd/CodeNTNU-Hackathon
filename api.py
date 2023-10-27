import requests
import json

url = 'https://kassal.app/api/v1/products'
headers = {
    'Authorization': 'Bearer 84fjqwPzO8TQgvw7bcUFhNubLBoCR0QBU7DktsNF'
}

params = {
    'search': 'rapsolje',
    'size': '100',
    'page': 3
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()

    # Store the response in a JSON file
    with open('products.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print('API response saved to products.json')
else:
    print(f'API request failed with status code {response.status_code}')
    print(response.text)
    
    
with open("products.json", "r") as f:
    data = json.loads(f.read())
    for store in data["data"]:
        print(store["name"])
    print()
