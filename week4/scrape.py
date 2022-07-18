import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1563476.html').read()
soup = BeautifulSoup(html,'html.parser')
spans = soup('span')
sum = 0
for span in spans:
    num = span.contents[0]
    num = int(num)
    sum+=num
print(sum)
