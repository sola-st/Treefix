# Extracted from ./data/repos/pandas/pandas/io/stata.py
for typ in self.typlist:
    self._write_bytes(struct.pack("B", typ))
