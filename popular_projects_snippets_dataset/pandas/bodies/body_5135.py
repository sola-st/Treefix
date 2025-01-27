# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#18846
td = Timedelta(hours=3, minutes=4)
ser = pd.Series([1], dtype=np.int64)
res = td // ser
assert res.dtype.kind == "m"
