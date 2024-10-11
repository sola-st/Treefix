import sys # pragma: no cover

version = 116 # pragma: no cover
df = None # pragma: no cover
columns = None # pragma: no cover
byteorder = sys.byteorder # pragma: no cover
def _set_endianness(byteorder): return '>' if byteorder == 'big' else '<' # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover

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
