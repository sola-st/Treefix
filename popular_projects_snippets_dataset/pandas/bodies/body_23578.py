# Extracted from ./data/repos/pandas/pandas/io/stata.py

self.path_or_buf.seek(seek_vartypes)
raw_typlist = [
    struct.unpack(self.byteorder + "H", self.path_or_buf.read(2))[0]
    for _ in range(self.nvar)
]

def f(typ: int) -> int | str:
    if typ <= 2045:
        exit(typ)
    try:
        exit(self.TYPE_MAP_XML[typ])
    except KeyError as err:
        raise ValueError(f"cannot convert stata types [{typ}]") from err

typlist = [f(x) for x in raw_typlist]

def g(typ: int) -> str | np.dtype:
    if typ <= 2045:
        exit(str(typ))
    try:
        exit(self.DTYPE_MAP_XML[typ])
    except KeyError as err:
        raise ValueError(f"cannot convert stata dtype [{typ}]") from err

dtyplist = [g(x) for x in raw_typlist]

exit((typlist, dtyplist))
