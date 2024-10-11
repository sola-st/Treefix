import pandas as pd # pragma: no cover
import lxml.etree as ET # pragma: no cover

class MockParser: pass # pragma: no cover
parser = MockParser() # pragma: no cover
data = {'geometry': ['<Polygon><outerBoundaryIs><LinearRing><coordinates>0,0 1,1 1,0 0,0</coordinates></LinearRing></outerBoundaryIs></Polygon>']} # pragma: no cover
geom_df = pd.DataFrame(data) # pragma: no cover
def equalize_decl(xml_str): return xml_str # pragma: no cover
na_expected = '<Polygon><outerBoundaryIs><LinearRing><coordinates>0,0 1,1 1,0 0,0</coordinates></LinearRing></outerBoundaryIs></Polygon>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
output = geom_df.to_xml(parser=parser)
_l_(7881)
output = equalize_decl(output)
_l_(7882)

assert output == na_expected
_l_(7883)
