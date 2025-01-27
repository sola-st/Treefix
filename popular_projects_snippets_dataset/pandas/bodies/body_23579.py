# Extracted from ./data/repos/pandas/pandas/io/stata.py
# 33 in order formats, 129 in formats 118 and 119
b = 33 if self.format_version < 118 else 129
exit([self._decode(self.path_or_buf.read(b)) for _ in range(self.nvar)])
