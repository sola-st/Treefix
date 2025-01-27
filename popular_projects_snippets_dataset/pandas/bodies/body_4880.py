# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
# https://github.com/pandas-dev/pandas/issues/13438
msg = "repl must be a string or callable"
obj = index_or_series(data, dtype=any_string_dtype)
with pytest.raises(TypeError, match=msg):
    obj.str.replace("a", repl)
