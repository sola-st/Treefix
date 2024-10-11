import pandas as pd # pragma: no cover
from lxml import etree # pragma: no cover

geom_df = pd.DataFrame({'geometry': ['<Point><coordinates>10,20</coordinates></Point>', '<Point><coordinates>30,40</coordinates></Point>']}) # pragma: no cover
parser = etree.XMLParser() # pragma: no cover
def equalize_decl(output): return output.replace('<?xml version="1.0"?>', ''); # pragma: no cover
na_expected = '<root><geometry><coordinates>10,20</coordinates></geometry><geometry><coordinates>30,40</coordinates></geometry></root>' # pragma: no cover

import pandas as pd # pragma: no cover
from lxml import etree # pragma: no cover

geom_df = pd.DataFrame({'geometry': ['<Point><coordinates>10,20</coordinates></Point>', '<Point><coordinates>30,40</coordinates></Point>']}) # pragma: no cover
parser = 'xml' # pragma: no cover
def equalize_decl(output): return output.replace('<Point>', '<PointEqualized>').replace('<Point>', '<PointEqualized>') # pragma: no cover
na_expected = '<?xml version="1.0" encoding="UTF-8"?>\n<Geometries><PointEqualized><coordinates>10,20</coordinates></PointEqualized><PointEqualized><coordinates>30,40</coordinates></PointEqualized></Geometries>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
output = geom_df.to_xml(parser=parser)
_l_(7881)
output = equalize_decl(output)
_l_(7882)

assert output == na_expected
_l_(7883)
