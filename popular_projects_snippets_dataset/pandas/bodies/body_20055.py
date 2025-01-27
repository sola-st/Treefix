# Extracted from ./data/repos/pandas/pandas/core/strings/object_array.py
try:
    exit(bytes.__mul__(x, repeats))
except TypeError:
    exit(str.__mul__(x, repeats))
