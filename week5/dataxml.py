import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
url = ' http://py4e-data.dr-chuck.net/comments_1563478.xml'
xml = urllib.request.urlopen(url)
data = xml.read()
tree = ET.fromstring(data)
sum = 0
count = 0
comments = tree.findall('comments/comment')
for comment in comments:
    count+=1
    num = comment.find('count').text
    sum+=float(num)
print(sum)
