# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
# https://github.com/pandas-dev/pandas/issues/10673
ser = Series(list("aabbcde"), dtype=any_string_dtype)
with pytest.raises(AttributeError, match="You cannot add any new attribute"):
    ser.str.xlabel = "a"
