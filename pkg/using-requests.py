import requests

url ='https://google.com'
response = requests.get(url)
print(f'Response returned: {response.status.code}, {response.reason}')
print(response.text)