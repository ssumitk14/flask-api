import requests
baseURL = "http://127.0.0.1:5000/"

data = [{"likes":20,"name":"First Video","views":100},
        {"likes":80,"name":"How to make first API","views":10000},
        {"likes":2,"name":"test video","views":48}]
for i in range(len(data)):
    response = requests.put(baseURL+'/Video/'+str(i) , data[i])
    print(response.json())

input()

response = requests.delete(baseURL+'Video/0')
print(response)
response = requests.get(baseURL+'/Video/2')
print(response.json())