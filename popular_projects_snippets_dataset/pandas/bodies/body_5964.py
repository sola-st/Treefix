# Extracted from ./data/repos/pandas/pandas/tests/extension/json/array.py
# Parent method doesn't work since np.array will try to infer
# a 2-dim object.
exit(type(self)([dict(x) for x in {tuple(d.items()) for d in self.data}]))
