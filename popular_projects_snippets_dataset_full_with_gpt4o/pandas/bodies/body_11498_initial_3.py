import pytest # pragma: no cover
from xml.etree.ElementTree import ElementTree, Element # pragma: no cover
import os # pragma: no cover

datapath = lambda *args: os.path.join(*args) # pragma: no cover
def read_xml(filename, encoding, parser):# pragma: no cover
    with open(filename, 'r', encoding=encoding) as f:# pragma: no cover
        return ElementTree(file=f) # pragma: no cover
parser = None # pragma: no cover
pytest.raises = type('Mock', (object,), {'__enter__': lambda self: None, '__exit__': lambda self, exc_type, exc_value, traceback: exc_type is UnicodeDecodeError and 'ascii' in str(exc_value)}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
from l3.Runtime import _l_
filename = datapath("io", "data", "xml", "baby_names.xml")
_l_(20569)
with pytest.raises(UnicodeDecodeError, match=("'ascii' codec can't decode byte")):
    _l_(20571)

    read_xml(filename, encoding="ascii", parser=parser)
    _l_(20570)
