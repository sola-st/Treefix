# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
a = cls._from_sequence(["a", None, "b"])
assert a[1] is not None
assert a[1] is pd.NA
