import urllib.error, urllib.request, urllib.parse
import json

url =  "http://py4e-data.dr-chuck.net/json?"
address=input('Enter Location: ' )
paramurl = url + urllib.parse.urlencode({"address": address, "key": 42})
jsn = urllib.request.urlopen(paramurl)
data = jsn.read()
js = json.loads(data)
print('Place_Id',js['results'][0]['place_id'])
