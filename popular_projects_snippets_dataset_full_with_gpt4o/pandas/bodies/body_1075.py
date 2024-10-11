# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py

# GH3777 part 2

# mixed dtype
df = DataFrame(
    np.random.randint(5, 10, size=9).reshape(3, 3),
    columns=list("abc"),
    index=[[4, 4, 8], [8, 10, 12]],
)
df["d"] = np.nan
arr = np.array([0.0, 1.0])

df.loc[4, "d"] = arr
tm.assert_series_equal(df.loc[4, "d"], Series(arr, index=[8, 10], name="d"))
