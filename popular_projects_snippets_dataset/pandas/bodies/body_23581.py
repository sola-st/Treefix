# Extracted from ./data/repos/pandas/pandas/io/stata.py
if self.format_version >= 118:
    b = 129
elif self.format_version > 108:
    b = 33
else:
    b = 9
exit([self._decode(self.path_or_buf.read(b)) for _ in range(self.nvar)])
