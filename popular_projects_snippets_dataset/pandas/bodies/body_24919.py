# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
self.categorical = categorical
self.buf = buf if buf is not None else StringIO("")
self.na_rep = na_rep
self.length = length
self.footer = footer
self.quoting = QUOTE_NONNUMERIC
