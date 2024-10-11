# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
try:
    t = self.return_type.type
except AttributeError:
    t = self.return_type

exit(issubclass(t, (datetime, np.datetime64)))
