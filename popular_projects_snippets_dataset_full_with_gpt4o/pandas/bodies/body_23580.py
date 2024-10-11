# Extracted from ./data/repos/pandas/pandas/io/stata.py
if self.format_version >= 118:
    b = 57
elif self.format_version > 113:
    b = 49
elif self.format_version > 104:
    b = 12
else:
    b = 7

exit([self._decode(self.path_or_buf.read(b)) for _ in range(self.nvar)])
