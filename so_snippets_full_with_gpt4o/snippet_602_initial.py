# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/749796/pretty-printing-xml-in-python
from l3.Runtime import _l_
try:
    import xml.dom.minidom
    _l_(13614)

except ImportError:
    pass

file = open("./content.xml", 'r')
_l_(13615)
xml_string = file.read()
_l_(13616)
file.close()
_l_(13617)

parsed_xml = xml.dom.minidom.parseString(xml_string)
_l_(13618)
pretty_xml_as_string = parsed_xml.toprettyxml()
_l_(13619)

file = open("./content_new.xml", 'w')
_l_(13620)
file.write(pretty_xml_as_string)
_l_(13621)
file.close()
_l_(13622)

