# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
s = Series(["foo,bar"])

result = s.apply(str.split, args=(",",))
assert result[0] == ["foo", "bar"]
assert isinstance(result[0], list)
