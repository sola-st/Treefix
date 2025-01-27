# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_dtypes.py
# see gh-22343
arr = pd.array([np.nan, 1, 2], dtype="Int8")
msg = "cannot convert NA to integer"

with pytest.raises(ValueError, match=msg):
    arr.astype("uint32")
