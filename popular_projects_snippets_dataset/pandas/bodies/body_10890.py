# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_counting.py
# GH#5610
# count counts non-nulls
df = DataFrame(
    [[1, 2, "foo"], [1, np.nan, "bar"], [3, np.nan, np.nan]],
    columns=["A", "B", "C"],
)

count_as = df.groupby("A").count()
count_not_as = df.groupby("A", as_index=False).count()

expected = DataFrame([[1, 2], [0, 0]], columns=["B", "C"], index=[1, 3])
expected.index.name = "A"
tm.assert_frame_equal(count_not_as, expected.reset_index())
tm.assert_frame_equal(count_as, expected)

count_B = df.groupby("A")["B"].count()
tm.assert_series_equal(count_B, expected["B"])
