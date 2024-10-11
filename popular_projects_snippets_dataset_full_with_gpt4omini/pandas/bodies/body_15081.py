# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
# gh-13258
# test if items yields the correct boxed scalars
# this only applies to series
s = Series([1], dtype=dtype)
_, result = list(s.items())[0]
assert isinstance(result, rdtype)

_, result = list(s.items())[0]
assert isinstance(result, rdtype)
