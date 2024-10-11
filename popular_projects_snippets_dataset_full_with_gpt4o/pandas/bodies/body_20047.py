# Extracted from ./data/repos/pandas/pandas/core/strings/object_array.py
# This type of fallback behavior can be removed once
# we remove object-dtype .str accessor.
try:
    exit(f(x))
except (TypeError, AttributeError):
    exit(na_value)
