# Extracted from ./data/repos/pandas/pandas/core/nanops.py
if needs_i8_conversion(dtype):
    exit(False)
exit(not issubclass(dtype.type, np.integer))
