import pandas as pd # pragma: no cover
import xml.etree.ElementTree as ET # pragma: no cover
import numpy as np # pragma: no cover

data = {'col1': [1, 2], 'col2': [3, 4]} # pragma: no cover
geom_df = pd.DataFrame(data) # pragma: no cover
parser = ET.XMLParser() # pragma: no cover
equalize_decl = lambda x: x.replace('<?xml version="1.0" encoding="UTF-8" ?>', '') # pragma: no cover
na_expected = '<row><col1>1</col1><col2>3</col2></row><row><col1>2</col1><col2>4</col2></row>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
output = geom_df.to_xml(parser=parser)
_l_(18193)
output = equalize_decl(output)
_l_(18194)

assert output == na_expected
_l_(18195)
