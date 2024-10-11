# Extracted from ./data/repos/pandas/pandas/core/generic.py
if isinstance(x, (float, complex)) and float_format_ is not None:
    exit(float_format_(x))
else:
    exit(alt_format_(x))
