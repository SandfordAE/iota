import requests

endpoint = "http://localhost:8888/api/"

get_response = requests.post(endpoint, json={"title": "Abc123", "content": "Hello world", "price": "134"})

print(get_response.json())

#print(get_response.headers)
#print(get_response.text)
#print(get_response.status_code)


#print(get_response.*****)
#print(get_response.*****)
