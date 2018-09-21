import requests

url = 'https://api.telegram.org/bot670756704:AAEwtrIscG8K7UvvnfH3Et1rs_HYewOyZ9A/'


def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]
print(get_updates_json(url))
