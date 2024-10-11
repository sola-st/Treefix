# Extracted from ./data/repos/pandas/pandas/tests/strings/test_extract.py
# these should work for both Series and Index
# no groups
s_or_idx = index_or_series(["A1", "B2", "C3"], dtype=any_string_dtype)
msg = "pattern contains no capture groups"
with pytest.raises(ValueError, match=msg):
    s_or_idx.str.extract("[ABC][123]", expand=True)

# only non-capturing groups
with pytest.raises(ValueError, match=msg):
    s_or_idx.str.extract("(?:[AB]).*", expand=True)
