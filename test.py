import requests

baseURL = "http://127.0.0.1:5000/"

data = requests.get(baseURL+'/test')
print(data.json())