# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
obj = index_or_series(
    ["ABCDEFG", "BCDEFEF", "DEFGHIJEF", "EFGHEF"], dtype=any_string_dtype
)
with pytest.raises(ValueError, match="substring not found"):
    obj.str.index("DE")
