import urllib.request, urllib.error, urllib.parse
import ssl
import xml.etree.ElementTree as ET

xml_url = 'http://py4e-data.dr-chuck.net/comments_514390.xml'

data = urllib.request.urlopen(xml_url).read().decode()
# print (data)

info = ET.fromstring(data)
lst = info.findall('comments/comment')
count = 0
for item in lst:
    a = float(item.find('count').text)
    count = a+ count

print (count)


