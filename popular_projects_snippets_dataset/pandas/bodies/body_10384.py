# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py

df = DataFrame({"id": np.arange(100000) / 3, "val": np.random.randn(100000)})

grp = df.groupby("id")["val"]

values = np.repeat(grp.mean().values, ensure_platform_int(grp.count().values))
expected = Series(values, index=df.index, name="val")

result = grp.transform(np.mean)
tm.assert_series_equal(result, expected)

result = grp.transform("mean")
tm.assert_series_equal(result, expected)

# GH 12737
df = DataFrame(
    {
        "grouping": [0, 1, 1, 3],
        "f": [1.1, 2.1, 3.1, 4.5],
        "d": date_range("2014-1-1", "2014-1-4"),
        "i": [1, 2, 3, 4],
    },
    columns=["grouping", "f", "i", "d"],
)
result = df.groupby("grouping").transform("first")

dates = [
    Timestamp("2014-1-1"),
    Timestamp("2014-1-2"),
    Timestamp("2014-1-2"),
    Timestamp("2014-1-4"),
]
expected = DataFrame(
    {"f": [1.1, 2.1, 2.1, 4.5], "d": dates, "i": [1, 2, 2, 4]},
    columns=["f", "i", "d"],
)
tm.assert_frame_equal(result, expected)

# selection
result = df.groupby("grouping")[["f", "i"]].transform("first")
expected = expected[["f", "i"]]
tm.assert_frame_equal(result, expected)

# dup columns
df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=["g", "a", "a"])
result = df.groupby("g").transform("first")
expected = df.drop("g", axis=1)
tm.assert_frame_equal(result, expected)
