import pytest # pragma: no cover
from lxml import etree # pragma: no cover
import os # pragma: no cover

def datapath(*paths): return os.path.join(*paths) # pragma: no cover
def read_xml(filename, encoding, parser): raise UnicodeDecodeError('ascii', b'', 0, 1, 'expected byte') # pragma: no cover
parser = etree.XMLParser() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
from l3.Runtime import _l_
filename = datapath("io", "data", "xml", "baby_names.xml")
_l_(9062)
with pytest.raises(UnicodeDecodeError, match=("'ascii' codec can't decode byte")):
    _l_(9064)

    read_xml(filename, encoding="ascii", parser=parser)
    _l_(9063)
