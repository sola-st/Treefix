# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py
# Ensure we don't leak file descriptors, but put in try/except in case
# attributes are already deleted
try:
    self.close()
except AttributeError:
    pass
