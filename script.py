import xml.etree.cElementTree as ET

tree = Et.ElementTree(file="input.xml")
root = tree.getroot()
for chld in root:
    print chld.get('id')