import requests

endpoint = "http://localhost:8888/api/products/38098498139/" 

get_response = requests.get(endpoint) 
print(get_response.json())