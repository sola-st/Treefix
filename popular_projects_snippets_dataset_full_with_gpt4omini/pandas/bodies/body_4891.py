# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
ser = Series([], dtype=any_string_dtype)
pat = re.compile("[a-z][A-Z]{2}")

msg = "Cannot use a compiled regex as replacement pattern with regex=False"
with pytest.raises(ValueError, match=msg):
    ser.str.replace(pat, "", regex=False)
