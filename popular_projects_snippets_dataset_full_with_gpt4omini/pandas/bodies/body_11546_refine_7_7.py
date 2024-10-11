import pandas as pd # pragma: no cover
from lxml import etree # pragma: no cover

geom_df = pd.DataFrame({'geometry': ['<Point>0 0</Point>', '<LineString>0 0, 1 1</LineString>']}) # pragma: no cover
parser = etree.XMLParser(recover=True) # pragma: no cover
def equalize_decl(xml_string): return xml_string.replace('Point', 'PointEqualized') # pragma: no cover
na_expected = '<root><PointEqualized>0 0</PointEqualized><LineString>0 0, 1 1</LineString></root>' # pragma: no cover

import pandas as pd # pragma: no cover
from lxml import etree # pragma: no cover

geom_df = pd.DataFrame({'geometry': ['<Point><coordinates>10,20</coordinates></Point>', '<LineString><coordinates>30,40 50,60</coordinates></LineString>']}) # pragma: no cover
parser = etree.XMLParser() # pragma: no cover
def equalize_decl(output): return output.replace('Point', 'PointEqualized').replace('LineString', 'LineStringEqualized') # pragma: no cover
na_expected = '<?xml version="1.0"?>\n<root><PointEqualized><coordinates>10,20</coordinates></PointEqualized><LineStringEqualized><coordinates>30,40 50,60</coordinates></LineStringEqualized></root>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
output = geom_df.to_xml(parser=parser)
_l_(7881)
output = equalize_decl(output)
_l_(7882)

assert output == na_expected
_l_(7883)
