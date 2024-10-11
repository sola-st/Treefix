# Extracted from ./data/repos/pandas/pandas/io/stata.py
self._update_map("sortlist")
sort_size = 2 if self._dta_version < 119 else 4
self._write_bytes(self._tag(b"\x00" * sort_size * (self.nvar + 1), "sortlist"))
