# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_to_offset.py
# see gh-9064
td = Timedelta(**kwargs)
result = to_offset(td)
assert result == expected
