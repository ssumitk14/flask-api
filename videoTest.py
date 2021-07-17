import requests
baseURL = "http://127.0.0.1:5000/"

response = requests.put(baseURL+'/Video/1' , {"likes":20})
print(response.json())