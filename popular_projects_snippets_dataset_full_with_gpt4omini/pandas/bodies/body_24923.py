# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
self.series = series
self.buf = buf if buf is not None else StringIO()
self.name = name
self.na_rep = na_rep
self.header = header
self.length = length
self.index = index
self.max_rows = max_rows
self.min_rows = min_rows

if float_format is None:
    float_format = get_option("display.float_format")
self.float_format = float_format
self.dtype = dtype
self.adj = get_adjustment()

self._chk_truncate()
