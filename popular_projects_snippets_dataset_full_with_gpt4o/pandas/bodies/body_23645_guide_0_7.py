import sys # pragma: no cover

version = 119 # pragma: no cover
df = None # pragma: no cover
columns = [] # pragma: no cover
byteorder = None # pragma: no cover
class ExampleClass: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._dta_ver = None # pragma: no cover
        self.df = None # pragma: no cover
        self.columns = None # pragma: no cover
        self._gso_table = None # pragma: no cover
        self._byteorder = None # pragma: no cover
        self._encoding = None # pragma: no cover
        self._o_offet = None # pragma: no cover
        self._gso_o_type = None # pragma: no cover
        self._gso_v_type = None # pragma: no cover
    def _set_endianness(self, byteorder): # pragma: no cover
        if byteorder == 'little': # pragma: no cover
            return 'little' # pragma: no cover
        else: # pragma: no cover
            return 'big' # pragma: no cover
example = ExampleClass() # pragma: no cover
self = example # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/stata.py
from l3.Runtime import _l_
if version not in (117, 118, 119):
    _l_(21788)

    raise ValueError("Only dta versions 117, 118 and 119 supported")
    _l_(21787)
self._dta_ver = version
_l_(21789)

self.df = df
_l_(21790)
self.columns = columns
_l_(21791)
self._gso_table = {"": (0, 0)}
_l_(21792)
if byteorder is None:
    _l_(21794)

    byteorder = sys.byteorder
    _l_(21793)
self._byteorder = _set_endianness(byteorder)
_l_(21795)

gso_v_type = "I"  # uint32
_l_(21796)  # uint32
gso_o_type = "Q"  # uint64
_l_(21797)  # uint64
self._encoding = "utf-8"
_l_(21798)
if version == 117:
    _l_(21805)

    o_size = 4
    _l_(21799)
    gso_o_type = "I"  # 117 used uint32
    _l_(21800)  # 117 used uint32
    self._encoding = "latin-1"
    _l_(21801)
elif version == 118:
    _l_(21804)

    o_size = 6
    _l_(21802)
else:  # version == 119
    o_size = 5
    _l_(21803)
self._o_offet = 2 ** (8 * (8 - o_size))
_l_(21806)
self._gso_o_type = gso_o_type
_l_(21807)
self._gso_v_type = gso_v_type
_l_(21808)
