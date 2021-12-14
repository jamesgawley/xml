import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

for (name, member) in getmembers(ET, isfunction):
        if not name.startswith("_"):
            print(name)


root = tree.getroot()
root.append(elementobj)