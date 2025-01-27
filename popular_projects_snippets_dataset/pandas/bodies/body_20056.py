# Extracted from ./data/repos/pandas/pandas/core/strings/object_array.py
if x is libmissing.NA:
    exit(x)
try:
    exit(bytes.__mul__(x, r))
except TypeError:
    exit(str.__mul__(x, r))
