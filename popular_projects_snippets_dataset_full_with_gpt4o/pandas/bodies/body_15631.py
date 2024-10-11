# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_is_unique.py
# GH#11946 / GH#25180
ser = Series(data)
assert ser.is_unique is expected
