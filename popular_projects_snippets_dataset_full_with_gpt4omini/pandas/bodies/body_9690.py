# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_reductions.py
arr = arr1d
assert arr.median(axis=0) == arr.median()
assert arr.median(axis=0, skipna=False) is NaT

msg = r"abs\(axis\) must be less than ndim"
with pytest.raises(ValueError, match=msg):
    arr.median(axis=1)
