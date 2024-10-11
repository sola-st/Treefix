import pandas as pd # pragma: no cover
import xml.etree.ElementTree as ET # pragma: no cover

geom_df = pd.DataFrame({'geometry': ['<Point><x>1</x><y>2</y></Point>, <Point><x>3</x><y>4</y></Point>']}) # pragma: no cover
parser = ET.XMLParser() # pragma: no cover
def equalize_decl(output): return output.replace('<Point>', '<NewPoint>').replace('</Point>', '</NewPoint>') # pragma: no cover
na_expected = '<NewPoint><x>1</x><y>2</y></NewPoint>, <NewPoint><x>3</x><y>4</y></NewPoint>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
output = geom_df.to_xml(parser=parser)
_l_(7881)
output = equalize_decl(output)
_l_(7882)

assert output == na_expected
_l_(7883)
