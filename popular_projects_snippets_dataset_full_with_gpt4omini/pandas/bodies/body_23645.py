# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/stata.py
from l3.Runtime import _l_
if version not in (117, 118, 119):
    _l_(10531)

    raise ValueError("Only dta versions 117, 118 and 119 supported")
    _l_(10530)
self._dta_ver = version
_l_(10532)

self.df = df
_l_(10533)
self.columns = columns
_l_(10534)
self._gso_table = {"": (0, 0)}
_l_(10535)
if byteorder is None:
    _l_(10537)

    byteorder = sys.byteorder
    _l_(10536)
self._byteorder = _set_endianness(byteorder)
_l_(10538)

gso_v_type = "I"  # uint32
_l_(10539)  # uint32
gso_o_type = "Q"  # uint64
_l_(10540)  # uint64
self._encoding = "utf-8"
_l_(10541)
if version == 117:
    _l_(10548)

    o_size = 4
    _l_(10542)
    gso_o_type = "I"  # 117 used uint32
    _l_(10543)  # 117 used uint32
    self._encoding = "latin-1"
    _l_(10544)
elif version == 118:
    _l_(10547)

    o_size = 6
    _l_(10545)
else:  # version == 119
    o_size = 5
    _l_(10546)
self._o_offet = 2 ** (8 * (8 - o_size))
_l_(10549)
self._gso_o_type = gso_o_type
_l_(10550)
self._gso_v_type = gso_v_type
_l_(10551)
