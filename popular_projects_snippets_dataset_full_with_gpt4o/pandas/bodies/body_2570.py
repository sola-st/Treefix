# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# assignment
df = DataFrame(
    {"value": np.array(np.random.randint(0, 10000, 100), dtype="int32")}
)
labels = Categorical([f"{i} - {i + 499}" for i in range(0, 10000, 500)])

df = df.sort_values(by=["value"], ascending=True)
ser = cut(df.value, range(0, 10500, 500), right=False, labels=labels)
cat = ser.values

# setting with a Categorical
df["D"] = cat
str(df)

result = df.dtypes
expected = Series(
    [np.dtype("int32"), CategoricalDtype(categories=labels, ordered=False)],
    index=["value", "D"],
)
tm.assert_series_equal(result, expected)

# setting with a Series
df["E"] = ser
str(df)

result = df.dtypes
expected = Series(
    [
        np.dtype("int32"),
        CategoricalDtype(categories=labels, ordered=False),
        CategoricalDtype(categories=labels, ordered=False),
    ],
    index=["value", "D", "E"],
)
tm.assert_series_equal(result, expected)

result1 = df["D"]
result2 = df["E"]
tm.assert_categorical_equal(result1._mgr.array, cat)

# sorting
ser.name = "E"
tm.assert_series_equal(result2.sort_index(), ser.sort_index())
