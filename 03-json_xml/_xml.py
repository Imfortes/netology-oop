import xml.etree.ElementTree as ET

tree_root = ET.parse('./03-json_xml/news.xml').getroot()

print(tree_root)

for tag in tree_root.findall('channel/item'):
    h_value = tag.get('item')
    print(tag.attrib)
    if h_value is not None: 
        print(h_value) 
    t_value = tag.get('text') 
    if t_value is not None: 
        print(t_value)