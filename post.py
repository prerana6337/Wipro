import requests
url="https://jsonplaceholder.typicode.com/posts"
data={
    "title":"hello",
    "body":"wipro",
    "userId":1
}
response = requests.post(url, json=data)
print("Status code:", response.status_code)
print("Response json:", response.json())