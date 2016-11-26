import xml.etree.cElementTree as ET 


tree= ET.ElementTree(file="input.xml")
root= tree.getroot()

for book in root:
    print(book.get("id"))
    for attr in book:
        if (attr.tag=="author" or attr.tag=="title" or attr.tag=="price"):
            print(attr.text)