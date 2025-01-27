# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
# GH3777 part 2b
# single dtype
arr = np.array([0.0, 1.0])

df = DataFrame(
    np.random.randint(5, 10, size=9).reshape(3, 3),
    columns=list("abc"),
    index=[[4, 4, 8], [8, 10, 12]],
    dtype=np.int64,
)
view = df["c"].iloc[:2].values

# arr can be losslessly cast to int, so this setitem is inplace
df.loc[4, "c"] = arr
exp = Series(arr, index=[8, 10], name="c", dtype="int64")
result = df.loc[4, "c"]
tm.assert_series_equal(result, exp)

# extra check for inplace-ness
if not using_copy_on_write:
    tm.assert_numpy_array_equal(view, exp.values)

# arr + 0.5 cannot be cast losslessly to int, so we upcast
df.loc[4, "c"] = arr + 0.5
result = df.loc[4, "c"]
exp = exp + 0.5
tm.assert_series_equal(result, exp)

# scalar ok
df.loc[4, "c"] = 10
exp = Series(10, index=[8, 10], name="c", dtype="float64")
tm.assert_series_equal(df.loc[4, "c"], exp)

# invalid assignments
msg = "Must have equal len keys and value when setting with an iterable"
with pytest.raises(ValueError, match=msg):
    df.loc[4, "c"] = [0, 1, 2, 3]

with pytest.raises(ValueError, match=msg):
    df.loc[4, "c"] = [0]

# But with a length-1 listlike column indexer this behaves like
#  `df.loc[4, "c"] = 0
df.loc[4, ["c"]] = [0]
assert (df.loc[4, "c"] == 0).all()
