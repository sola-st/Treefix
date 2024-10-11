import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
from lxml import etree # pragma: no cover

geom_df = pd.DataFrame({'geometry': ['<Polygon><x>1</x><y>2</y></Polygon>']}) # pragma: no cover
parser = etree.XMLParser() # pragma: no cover
na_expected = '<Polygon><x>1</x><y>2</y></Polygon>' # pragma: no cover
def equalize_decl(xml_string): return xml_string # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
output = geom_df.to_xml(parser=parser)
_l_(7881)
output = equalize_decl(output)
_l_(7882)

assert output == na_expected
_l_(7883)
