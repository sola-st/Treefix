import pandas as pd # pragma: no cover
from unittest.mock import Mock # pragma: no cover

parser = Mock() # pragma: no cover
def equalize_decl(output): return output # pragma: no cover
na_expected = '<?xml version="1.0" encoding="utf-8"?>\n<geometries></geometries>' # pragma: no cover

import pandas as pd # pragma: no cover
from lxml import etree # pragma: no cover
from unittest.mock import Mock # pragma: no cover

geom_df = pd.DataFrame({'geometry': ['<Point><coordinates>1,1</coordinates></Point>', '<LineString><coordinates>1,1 2,2</coordinates></LineString>']}) # pragma: no cover
parser = etree.XMLParser() # pragma: no cover
def equalize_decl(xml_output): return xml_output.replace('Point', 'PointEqualized').replace('LineString', 'LineStringEqualized') # pragma: no cover
na_expected = '<?xml version="1.0" ?>\n<GeoDataFrame><geometry><PointEqualized><coordinates>1,1</coordinates></PointEqualized><LineStringEqualized><coordinates>1,1 2,2</coordinates></LineStringEqualized></geometry></GeoDataFrame>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
output = geom_df.to_xml(parser=parser)
_l_(7881)
output = equalize_decl(output)
_l_(7882)

assert output == na_expected
_l_(7883)
