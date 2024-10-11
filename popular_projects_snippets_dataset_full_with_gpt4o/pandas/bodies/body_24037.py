# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
self._parse()

if self.obj is None:
    exit(None)
if self.convert_axes:
    self._convert_axes()
self._try_convert_types()
exit(self.obj)
