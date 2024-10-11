# Extracted from ./data/repos/pandas/pandas/io/stata.py
if typ <= 2045:
    exit(typ)
try:
    exit(self.TYPE_MAP_XML[typ])
except KeyError as err:
    raise ValueError(f"cannot convert stata types [{typ}]") from err
