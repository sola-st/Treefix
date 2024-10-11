# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
ser = Series([], dtype=any_string_dtype)
repl = lambda m: m.group(0).swapcase()

msg = "Cannot use a callable replacement when regex=False"
with pytest.raises(ValueError, match=msg):
    ser.str.replace("abc", repl, regex=False)
