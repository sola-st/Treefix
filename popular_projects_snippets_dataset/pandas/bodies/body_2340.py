# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
dti = date_range("2016-01-01", periods=6)
dta = dti._data.reshape(3, 2)
other = dta - dta[0, 0]

df = DataFrame(dta, columns=["A", "B"])

mask = np.asarray(df.isna())
mask[:, 1] = True

# setting all of one column, none of the other
expected = DataFrame({"A": other[:, 0], "B": dta[:, 1]})
_check_where_equivalences(df, mask, other, expected)

# setting part of one column, none of the other
mask[1, 0] = True
expected = DataFrame(
    {
        "A": np.array([other[0, 0], dta[1, 0], other[2, 0]], dtype=object),
        "B": dta[:, 1],
    }
)
_check_where_equivalences(df, mask, other, expected)

# setting nothing in either column
mask[:] = True
expected = df
_check_where_equivalences(df, mask, other, expected)
