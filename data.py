import requests

dict_params = {
    "amount": 10,
    "difficulty": "medium",
    "type": "boolean"
}

request = requests.get("https://opentdb.com/api.php", params=dict_params)
request.raise_for_status()
data = request.json()
question_data = data["results"]