import pandas as pd # pragma: no cover
from lxml import etree # pragma: no cover
import numpy as np # pragma: no cover

geom_df = pd.DataFrame({# pragma: no cover
    'id': [1, 2, 3],# pragma: no cover
    'geometry': ['POINT (1 1)', 'POINT (2 2)', 'POINT (3 3)']# pragma: no cover
}) # pragma: no cover
parser = etree.XMLParser() # pragma: no cover
def equalize_decl(xml_str):# pragma: no cover
    return xml_str.replace("<?xml version='1.0' encoding='utf-8'?>", "<?xml version='1.0'?>") # pragma: no cover
na_expected = '<?xml version="1.0"?><Data><id>1</id><geometry>POINT (1 1)</geometry></Data><Data><id>2</id><geometry>POINT (2 2)</geometry></Data><Data><id>3</id><geometry>POINT (3 3)</geometry></Data>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
output = geom_df.to_xml(parser=parser)
_l_(18193)
output = equalize_decl(output)
_l_(18194)

assert output == na_expected
_l_(18195)
