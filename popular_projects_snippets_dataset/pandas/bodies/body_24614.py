# Extracted from ./data/repos/pandas/pandas/io/formats/csvs.py
if self._need_to_save_header:
    self._save_header()
self._save_body()
