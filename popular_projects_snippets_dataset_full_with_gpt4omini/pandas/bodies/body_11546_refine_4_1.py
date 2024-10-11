import pandas as pd # pragma: no cover
from io import StringIO # pragma: no cover

geom_df = pd.DataFrame({'geometry': ['<Point><coordinates>1,2</coordinates></Point>']}) # pragma: no cover
parser = StringIO() # pragma: no cover
def equalize_decl(output): return output # pragma: no cover
na_expected = '<Point><coordinates>1,2</coordinates></Point>' # pragma: no cover

import pandas as pd # pragma: no cover
from lxml import etree # pragma: no cover

geom_df = pd.DataFrame({'geometry': ['<Point><coordinates>1.0,2.0</coordinates></Point>', '<Point><coordinates>3.0,4.0</coordinates></Point>']}) # pragma: no cover
parser = etree.XMLParser(recover=True) # pragma: no cover
def equalize_decl(output): return output.replace('<Point>', '<Point equalized>').replace('</Point>', '</Point equalized>') # pragma: no cover
na_expected = '<GeometryCollection><Point equalized><coordinates>1.0,2.0</coordinates></Point equalized><Point equalized><coordinates>3.0,4.0</coordinates></Point equalized></GeometryCollection>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
output = geom_df.to_xml(parser=parser)
_l_(7881)
output = equalize_decl(output)
_l_(7882)

assert output == na_expected
_l_(7883)
