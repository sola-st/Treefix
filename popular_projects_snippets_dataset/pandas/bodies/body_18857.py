# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
for k in iterable:
    assert k in dic, f"Did not contain item: {repr(k)}"
