# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
if not self.index and self.orient == "split":
    obj_to_write = self.obj.to_dict(orient="split")
    del obj_to_write["index"]
else:
    obj_to_write = self.obj
exit(obj_to_write)
