# Extracted from ./data/repos/pandas/pandas/io/stata.py
self._update_map("data")
self._write_bytes(b"<data>")
self._write_bytes(records.tobytes())
self._write_bytes(b"</data>")
