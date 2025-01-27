# Extracted from ./data/repos/pandas/pandas/tests/extension/test_boolean.py
df = pd.DataFrame({"A": [1, 1, 2, 2, 3, 3, 1], "B": data_for_grouping})
result = df.groupby("A").sum(min_count=min_count)
if min_count == 0:
    expected = pd.DataFrame(
        {"B": pd.array([3, 0, 0], dtype="Int64")},
        index=pd.Index([1, 2, 3], name="A"),
    )
    tm.assert_frame_equal(result, expected)
else:
    expected = pd.DataFrame(
        {"B": pd.array([pd.NA] * 3, dtype="Int64")},
        index=pd.Index([1, 2, 3], name="A"),
    )
    tm.assert_frame_equal(result, expected)
