import requests
baseURL = "http://127.0.0.1:5000/"
'''
data = [{"name":"First Video","views":100,"likes":20},
        {"name":"How to make first API","views":10000,"likes":80},
        {"name":"test video","views":48,"likes":2}]

for i in range(len(data)):
    response = requests.put(baseURL+'/Video/'+str(i),data[i],verify=False)
    print(response.json())

input()


response = requests.get(baseURL+'/Video/1')
print(response.json())'''

response = requests.get(baseURL+'/Video/1')
print(response.json())
input()
response = requests.patch(baseURL+'/Video/1',{'likes':102})
print(response.json())