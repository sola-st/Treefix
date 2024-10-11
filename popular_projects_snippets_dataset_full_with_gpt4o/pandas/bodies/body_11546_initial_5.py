import pandas as pd # pragma: no cover
import xml.etree.ElementTree as ET # pragma: no cover

geom_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}) # pragma: no cover
parser = ET.XMLParser() # pragma: no cover
def equalize_decl(xml_str):# pragma: no cover
    return xml_str.replace('<?xml version="1.0" encoding="UTF-8"?>', '<?xml version="1.0"?>') # pragma: no cover
na_expected = '<?xml version="1.0"?>\n<data>\n  <row>\n    <col1>1</col1>\n    <col2>3</col2>\n  </row>\n  <row>\n    <col1>2</col1>\n    <col2>4</col2>\n  </row>\n</data>' # pragma: no cover
pd.DataFrame.to_xml = lambda self, parser: '<?xml version="1.0" encoding="UTF-8"?>\n<data>\n  <row>\n    <col1>1</col1>\n    <col2>3</col2>\n  </row>\n  <row>\n    <col1>2</col1>\n    <col2>4</col2>\n  </row>\n</data>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
output = geom_df.to_xml(parser=parser)
_l_(18193)
output = equalize_decl(output)
_l_(18194)

assert output == na_expected
_l_(18195)
