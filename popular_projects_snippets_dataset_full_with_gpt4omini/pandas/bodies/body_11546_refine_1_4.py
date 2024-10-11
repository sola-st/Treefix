import pandas as pd # pragma: no cover
from unittest.mock import Mock # pragma: no cover

parser = Mock() # pragma: no cover
def equalize_decl(output): return output # pragma: no cover
na_expected = '<?xml version="1.0" encoding="utf-8"?>\n<geometries></geometries>' # pragma: no cover

import pandas as pd # pragma: no cover

parser = 'lxml' # pragma: no cover
def equalize_decl(output): return output.replace('POINT', 'POINTEqualized').replace('LINESTRING', 'LINESTRINGEqualized') # pragma: no cover
na_expected = '<?xml version="1.0" encoding="utf-8"?>\n<geometries><geometry>POINTEqualized (1 1)</geometry><geometry>LINESTRINGEqualized (1 1, 2 2)</geometry></geometries>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
output = geom_df.to_xml(parser=parser)
_l_(7881)
output = equalize_decl(output)
_l_(7882)

assert output == na_expected
_l_(7883)
