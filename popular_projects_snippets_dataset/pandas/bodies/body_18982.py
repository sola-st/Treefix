# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
try:
    t = self.type.type
except AttributeError:
    t = self.type

exit(issubclass(t, (datetime, np.datetime64)))
