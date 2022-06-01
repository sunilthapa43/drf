import requests

#endpoint = "https://httpbin.org/anything" 
endpoint = "http://localhost:8000/api/?abs=123"      #so we want to send what we build onwards

get_response = requests.get(endpoint, params = {"abs":123},json = {"product_id": 13} )

#print(get_response.text)

print(get_response.json())

print(get_response.status_code)