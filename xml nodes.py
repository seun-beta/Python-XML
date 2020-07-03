import xml.etree.ElementTree as ET
data ='''
<stuff>
<eng>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</eng>
</stuff>'''

info = ET.fromstring(data)
info_list = info.findall('eng/users/user')
print (info_list)
print()
for node in info_list:
    print (node.find('id').text)
    print (node.find('name').text)
    print (node.get('x'))
