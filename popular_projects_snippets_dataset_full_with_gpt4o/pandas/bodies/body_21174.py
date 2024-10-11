# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/accessor.py
if name == "from_coo":
    exit(self.from_coo(*args, **kwargs))
elif name == "to_coo":
    exit(self.to_coo(*args, **kwargs))
else:
    raise ValueError
