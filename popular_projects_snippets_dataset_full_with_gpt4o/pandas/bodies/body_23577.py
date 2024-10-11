# Extracted from ./data/repos/pandas/pandas/io/stata.py
if typ <= 2045:
    exit(str(typ))
try:
    exit(self.DTYPE_MAP_XML[typ])
except KeyError as err:
    raise ValueError(f"cannot convert stata dtype [{typ}]") from err
