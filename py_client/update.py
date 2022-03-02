import requests

endpoint = "http://localhost:8888/api/products/1/update/" 

data = {
    "title": "Hello world again",
    "price": 129.00
}

get_response = requests.put(endpoint, json=data) 
print(get_response.json())