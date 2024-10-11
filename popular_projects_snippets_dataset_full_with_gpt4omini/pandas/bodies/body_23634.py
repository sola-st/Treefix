# Extracted from ./data/repos/pandas/pandas/io/stata.py
# srtlist, 2*(nvar+1), int array, encoded by byteorder
srtlist = _pad_bytes("", 2 * (self.nvar + 1))
self._write(srtlist)
