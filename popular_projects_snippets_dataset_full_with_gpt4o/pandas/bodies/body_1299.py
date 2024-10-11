# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py
cat = Series(Categorical([1, 2, 3, 4]))
reverse = cat[::-1]
exp = np.array([4, 3, 2, 1], dtype=np.int64)
tm.assert_numpy_array_equal(reverse.__array__(), exp)

df = DataFrame({"value": (np.arange(100) + 1).astype("int64")})
df["D"] = pd.cut(df.value, bins=[0, 25, 50, 75, 100])

expected = Series([11, Interval(0, 25)], index=["value", "D"], name=10)
result = df.iloc[10]
tm.assert_series_equal(result, expected)

expected = DataFrame(
    {"value": np.arange(11, 21).astype("int64")},
    index=np.arange(10, 20).astype("int64"),
)
expected["D"] = pd.cut(expected.value, bins=[0, 25, 50, 75, 100])
result = df.iloc[10:20]
tm.assert_frame_equal(result, expected)

expected = Series([9, Interval(0, 25)], index=["value", "D"], name=8)
result = df.loc[8]
tm.assert_series_equal(result, expected)
