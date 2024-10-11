import pandas as pd # pragma: no cover
from io import StringIO # pragma: no cover

geom_df = pd.DataFrame({'geometry': ['<Point><coordinates>30,10</coordinates></Point>', '<Point><coordinates>40,20</coordinates></Point>']}) # pragma: no cover
parser = StringIO() # pragma: no cover
def equalize_decl(output): return output.replace('<Point>', '<Point equalize="True">') # pragma: no cover
na_expected = '<Point equalize="True"><coordinates>30,10</coordinates></Point><Point equalize="True"><coordinates>40,20</coordinates></Point>' # pragma: no cover

import pandas as pd # pragma: no cover
from lxml import etree # pragma: no cover

geom_df = pd.DataFrame({'geometry': ['<Point><coordinates>10,20</coordinates></Point>', '<LineString><coordinates>30,40 50,60</coordinates></LineString>']}) # pragma: no cover
parser = etree.XMLParser() # pragma: no cover
def equalize_decl(output): return output.replace('<Point>', '<Point equalized>').replace('<LineString>', '<LineString equalized>') # pragma: no cover
na_expected = '<?xml version="1.0"?>\n<geometries><Point equalized><coordinates>10,20</coordinates></Point equalized><LineString equalized><coordinates>30,40 50,60</coordinates></LineString equalized></geometries>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
output = geom_df.to_xml(parser=parser)
_l_(7881)
output = equalize_decl(output)
_l_(7882)

assert output == na_expected
_l_(7883)
