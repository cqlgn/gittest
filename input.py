import requests
import re
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
url = 'https://jinshuju.net/f/EwZkQr'
res = requests.get(url, headers=headers).text
#print(res)
print (type(res))
# repatern = "apiCode":"field_6"
regular= re.match(r'幼儿姓名.*\s.*(field_\d)',res)
print(regular)

