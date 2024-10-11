# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
arr = Series(["car", "house", "tree", "1"])
msg = r"invalid literal for int\(\) with base 10: 'car'"
with pytest.raises(ValueError, match=msg):
    arr.astype(dtype)
