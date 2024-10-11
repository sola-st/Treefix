import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
from lxml import etree # pragma: no cover

parser = etree.XMLParser() # pragma: no cover
geom_df = pd.DataFrame({'geometry': ['<Point><coordinates>1,1</coordinates></Point>', '<Point><coordinates>2,2</coordinates></Point>']}) # pragma: no cover
na_expected = '<root><geometry>&lt;Point&gt;&lt;coordinates&gt;1,1&lt;/coordinates&gt;&lt;/Point&gt;</geometry><geometry>&lt;Point&gt;&lt;coordinates&gt;2,2&lt;/coordinates&gt;&lt;/Point&gt;</geometry></root>' # pragma: no cover
def equalize_decl(output): return output.replace('&', '&amp;') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
output = geom_df.to_xml(parser=parser)
_l_(7881)
output = equalize_decl(output)
_l_(7882)

assert output == na_expected
_l_(7883)
