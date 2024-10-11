# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
ser = pd.Series(np.arange(5), dtype="int64")

def check_replace(to_rep, val, expected):
    sc = ser.copy()
    result = ser.replace(to_rep, val)
    return_value = sc.replace(to_rep, val, inplace=True)
    assert return_value is None
    tm.assert_series_equal(expected, result)
    tm.assert_series_equal(expected, sc)

# 3.0 can still be held in our int64 series, so we do not upcast GH#44940
tr, v = [3], [3.0]
check_replace(tr, v, ser)
# Note this matches what we get with the scalars 3 and 3.0
check_replace(tr[0], v[0], ser)

# MUST upcast to float
e = pd.Series([0, 1, 2, 3.5, 4])
tr, v = [3], [3.5]
check_replace(tr, v, e)

# casts to object
e = pd.Series([0, 1, 2, 3.5, "a"])
tr, v = [3, 4], [3.5, "a"]
check_replace(tr, v, e)

# again casts to object
e = pd.Series([0, 1, 2, 3.5, pd.Timestamp("20130101")])
tr, v = [3, 4], [3.5, pd.Timestamp("20130101")]
check_replace(tr, v, e)

# casts to object
e = pd.Series([0, 1, 2, 3.5, True], dtype="object")
tr, v = [3, 4], [3.5, True]
check_replace(tr, v, e)

# test an object with dates + floats + integers + strings
dr = pd.Series(pd.date_range("1/1/2001", "1/10/2001", freq="D"))
result = dr.astype(object).replace([dr[0], dr[1], dr[2]], [1.0, 2, "a"])
expected = pd.Series([1.0, 2, "a"] + dr[3:].tolist(), dtype=object)
tm.assert_series_equal(result, expected)
