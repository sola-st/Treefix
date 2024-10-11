import os # pragma: no cover
import pytest # pragma: no cover

datapath = lambda *args: os.path.join('some_base_path', *args) # pragma: no cover
parser = 'some_parser_object' # pragma: no cover
pytest.raises = type('Mock', (object,), {'__enter__': lambda s: s, '__exit__': lambda s, e_type, e_value, tb: e_type == UnicodeDecodeError}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
from l3.Runtime import _l_
filename = datapath("io", "data", "xml", "baby_names.xml")
_l_(20569)
with pytest.raises(UnicodeDecodeError, match=("'ascii' codec can't decode byte")):
    _l_(20571)

    read_xml(filename, encoding="ascii", parser=parser)
    _l_(20570)
