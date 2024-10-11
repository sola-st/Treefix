# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
# gh-10904
# gh-13258
# coerce iteration to underlying python / pandas types
typ = index_or_series
s = typ([obj], dtype=dtype)
result = method(s)[0]
assert isinstance(result, rdtype)
