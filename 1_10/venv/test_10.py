import requests

# Public API: JSONPlaceholder
url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

assert response.status_code == 200
assert 'id' in response.json()
assert response.json()['title']=='sunt aut facere repellat provident occaecati excepturi optio reprehenderit'
# print("Status Code:", response.status_code)
# print("Response JSON:", response.json())