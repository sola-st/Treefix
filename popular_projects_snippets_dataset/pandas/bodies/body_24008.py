# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
if not self.obj.index.is_unique and self.orient == "index":
    raise ValueError(f"Series index must be unique for orient='{self.orient}'")
