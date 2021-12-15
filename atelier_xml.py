import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

for (name, member) in getmembers(ET, isfunction):
        if not name.startswith("_"):
            print(name)

# parse the document
tree = ET.parse("xml/simple.xml")

#manipulate the root element
root = tree.getroot()
# print(ET.tostring(root))

#create a new element from text
elementobj = ET.fromstring("<name>Mr. Awesome</name>")

#add new element to the DOM
root.append(elementobj)

#write the new XML file
tree.write("doc.xml")

#alternate way of adding tags:

#create element without text
elementobj = ET.Element("tag")
elementobj.text = "text"
root.append(elementobj)

#find an element with a particular attribute
foundobj = tree.find(".//tagname[@n='value']")

#find an element with a particular text value
foundobj = tree.find("[name='Mr. Awesome']")

# look at an attribute
elementobj.attrib['attrib_name']

# remove an element
foundobj = 