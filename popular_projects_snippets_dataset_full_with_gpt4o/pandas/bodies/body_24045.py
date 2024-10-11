# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
if self.obj is None:
    exit()
obj, result = self._try_convert_data(
    "data", self.obj, convert_dates=self.convert_dates
)
if result:
    self.obj = obj
