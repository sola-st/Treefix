import pandas as pd # pragma: no cover
from io import StringIO # pragma: no cover

geom_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}) # pragma: no cover
parser = StringIO('<root><item>Expected Output</item></root>') # pragma: no cover
output = '<root><item>Expected Output</item></root>' # pragma: no cover
def equalize_decl(output): return output.replace('Expected Output', 'Expected Output') # pragma: no cover
na_expected = '<root><item>Expected Output</item></root>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
output = geom_df.to_xml(parser=parser)
_l_(7881)
output = equalize_decl(output)
_l_(7882)

assert output == na_expected
_l_(7883)
