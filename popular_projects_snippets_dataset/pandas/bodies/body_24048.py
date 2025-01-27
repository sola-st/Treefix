# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
if self.obj is None:
    exit()
if self.convert_dates:
    self._try_convert_dates()

self._process_converter(
    lambda col, c: self._try_convert_data(col, c, convert_dates=False)
)
