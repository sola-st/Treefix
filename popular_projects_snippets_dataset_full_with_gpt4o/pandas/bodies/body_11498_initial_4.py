import pytest # pragma: no cover
from pandas import read_xml # pragma: no cover

datapath = lambda *args: '/'.join(args) # pragma: no cover
parser = type('Mock', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
from l3.Runtime import _l_
filename = datapath("io", "data", "xml", "baby_names.xml")
_l_(20569)
with pytest.raises(UnicodeDecodeError, match=("'ascii' codec can't decode byte")):
    _l_(20571)

    read_xml(filename, encoding="ascii", parser=parser)
    _l_(20570)
