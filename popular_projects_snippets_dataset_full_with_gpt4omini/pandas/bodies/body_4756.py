# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
obj = index_or_series([], dtype=any_string_dtype)
msg = "expected a string object, not int"

with pytest.raises(TypeError, match=msg):
    getattr(obj.str, method)(0)
