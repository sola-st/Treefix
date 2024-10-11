# Extracted from ./data/repos/pandas/pandas/tests/strings/test_extract.py
# Does not make sense to use extractall with a regex that has no capture groups.
# (it returns DataFrame with one column for each capture group)
s = Series(["a3", "b3", "d4c2"], name="series_name", dtype=any_string_dtype)
with pytest.raises(ValueError, match="no capture groups"):
    s.str.extractall(r"[a-z]")
