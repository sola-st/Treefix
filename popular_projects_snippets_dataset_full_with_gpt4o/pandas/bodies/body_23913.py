# Extracted from ./data/repos/pandas/pandas/io/pytables.py
super().write(obj, **kwargs)
self.write_index("index", obj.index)
self.write_array("values", obj)
self.attrs.name = obj.name
