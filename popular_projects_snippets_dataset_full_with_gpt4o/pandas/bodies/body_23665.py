# Extracted from ./data/repos/pandas/pandas/io/stata.py
self._update_map("stata_data_close")
self._write_bytes(bytes("</stata_dta>", "utf-8"))
self._update_map("end-of-file")
