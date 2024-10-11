# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
if not self.index and self.orient == "split":
    exit({"name": self.obj.name, "data": self.obj.values})
else:
    exit(self.obj)
