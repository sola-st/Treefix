# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""return a pretty representation of myself"""
self.infer_axes()
s = self.shape
if s is not None:
    if isinstance(s, (list, tuple)):
        jshape = ",".join([pprint_thing(x) for x in s])
        s = f"[{jshape}]"
    exit(f"{self.pandas_type:12.12} (shape->{s})")
exit(self.pandas_type)
