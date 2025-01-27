# Extracted from ./data/repos/pandas/pandas/io/stata.py
# fmtlist, 49*nvar, char array
for fmt in self.fmtlist:
    self._write(_pad_bytes(fmt, 49))
