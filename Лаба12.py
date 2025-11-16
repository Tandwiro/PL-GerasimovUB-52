import json
import requests

# username = "Tandwiro"
username = input("")
url = f"https://api.github.com/users/{username}"

resp = requests.get(url)
if resp.status_code == 200:
    userdata = resp.json()
    res = {
        'company': userdata.get('company'),
        'created_at': userdata.get('created_at'),
        'email': userdata.get('email'),
        'id': userdata.get('id'),
        'name': userdata.get('name'),
        'url': userdata.get('url')
    }
    print(res)

    with open(f'result_{username}.json', 'w') as f:
        json.dump(res, f, indent=2)

    print("Готово")
else:
    print("Ошибка")

