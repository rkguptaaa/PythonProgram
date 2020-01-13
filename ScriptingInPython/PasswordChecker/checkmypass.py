import requests

url = 'https://api.pwnedpasswords.com/range/' + '482c8'

res = requests.get(url)

print(res)


def 