# Extracted from ./data/repos/pandas/pandas/io/stata.py
if isinstance(fmt, int):
    exit(fmt)
exit(struct.calcsize(self.byteorder + fmt))
