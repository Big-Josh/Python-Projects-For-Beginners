import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '233557174168',
  'message': 'Hello world',
  'key': 'textbelt',
})
print(resp.json())