import urllib.request,urllib.parse,urllib.error
import json
url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1563479.json')
data= url.read()
info = json.loads(data)
# print(info)
info = info['comments']
sum=0
for item in info:
    # print(item)
    # print('Count:', item['count'])
    sum+=int(item['count'])
print(sum)
