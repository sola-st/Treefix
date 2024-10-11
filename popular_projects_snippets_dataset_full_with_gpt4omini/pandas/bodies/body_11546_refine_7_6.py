import pandas as pd # pragma: no cover
from lxml import etree # pragma: no cover

geom_df = pd.DataFrame({'geometry': ['<Point>0 0</Point>', '<LineString>0 0, 1 1</LineString>']}) # pragma: no cover
parser = etree.XMLParser(recover=True) # pragma: no cover
def equalize_decl(xml_string): return xml_string.replace('Point', 'PointEqualized') # pragma: no cover
na_expected = '<root><PointEqualized>0 0</PointEqualized><LineString>0 0, 1 1</LineString></root>' # pragma: no cover

import pandas as pd # pragma: no cover
from lxml import etree # pragma: no cover

geom_df = pd.DataFrame({'geometry': ['<Point><coordinates>1,2</coordinates></Point>', '<Point><coordinates>3,4</coordinates></Point>']}) # pragma: no cover
parser = 'lxml' # pragma: no cover
def equalize_decl(output): return output.replace('<Point>', '<PointEqualized>').replace('</Point>', '</PointEqualized>') # pragma: no cover
na_expected = '<root><PointEqualized><coordinates>1,2</coordinates></PointEqualized><PointEqualized><coordinates>3,4</coordinates></PointEqualized></root>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
output = geom_df.to_xml(parser=parser)
_l_(7881)
output = equalize_decl(output)
_l_(7882)

assert output == na_expected
_l_(7883)
