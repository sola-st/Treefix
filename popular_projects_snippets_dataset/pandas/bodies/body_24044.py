# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
data = loads(self.json, precise_float=self.precise_float)

if self.orient == "split":
    decoded = {str(k): v for k, v in data.items()}
    self.check_keys_split(decoded)
    self.obj = Series(**decoded)
else:
    self.obj = Series(data)
