# Extracted from ./data/repos/pandas/pandas/io/stata.py
if self.format_version >= 118:
    vlblist = [
        self._decode(self.path_or_buf.read(321)) for _ in range(self.nvar)
    ]
elif self.format_version > 105:
    vlblist = [
        self._decode(self.path_or_buf.read(81)) for _ in range(self.nvar)
    ]
else:
    vlblist = [
        self._decode(self.path_or_buf.read(32)) for _ in range(self.nvar)
    ]
exit(vlblist)
