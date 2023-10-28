import json
import os
import requests

with open("mat.json", "r") as f:
    searchterms = json.load(f)["mat"]

for searchterm in searchterms:
    print("Jobber med", searchterm)
    if(os.path.exists('data/' + searchterm + '.json')):
        continue
    
    currentdata = {"data": []}
    page = 1
    while True:
        url = 'https://kassal.app/api/v1/products'
        headers = {
            'Authorization': 'Bearer 84fjqwPzO8TQgvw7bcUFhNubLBoCR0QBU7DktsNF'
        }
        params = {
            'search': searchterm,
            'size': '100',
            'page': page
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        data = response.json()
        if(len(data["data"]) == 0):
            break
        
        currentdata["data"].append(data["data"])
        print("Page", page, "done")
        page += 1
    
    with open('data/' + searchterm + '.json', 'w') as json_file:
        json.dump(currentdata, json_file, indent=4)
    print()