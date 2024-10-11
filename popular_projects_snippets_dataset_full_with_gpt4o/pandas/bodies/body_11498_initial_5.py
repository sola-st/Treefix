import pytest # pragma: no cover
from unittest.mock import Mock # pragma: no cover

datapath = lambda *args: '/'.join(args) # pragma: no cover
read_xml = Mock() # pragma: no cover
parser = Mock() # pragma: no cover
pytest = type('Mock', (object,), {'raises': Mock()}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
from l3.Runtime import _l_
filename = datapath("io", "data", "xml", "baby_names.xml")
_l_(20569)
with pytest.raises(UnicodeDecodeError, match=("'ascii' codec can't decode byte")):
    _l_(20571)

    read_xml(filename, encoding="ascii", parser=parser)
    _l_(20570)
