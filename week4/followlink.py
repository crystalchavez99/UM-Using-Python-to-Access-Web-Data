import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = 'http://py4e-data.dr-chuck.net/known_by_Shayaan.html'
for i in range(7):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    count = 0
    for tag in tags:
        count +=1
        if count > 18:
            break
        url = tag.get('href',None)
print(url)
