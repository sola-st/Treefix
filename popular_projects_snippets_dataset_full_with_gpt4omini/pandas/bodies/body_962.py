# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval.py
# GH#27456
ii = IntervalIndex.from_arrays(
    [0, 1, 10, 11, 0, 1, 10, 11], [1, 2, 11, 12, 1, 2, 11, 12], name="MP"
)
idx = pd.MultiIndex.from_arrays(
    [
        pd.Index(["FC", "FC", "FC", "FC", "OWNER", "OWNER", "OWNER", "OWNER"]),
        pd.Index(
            ["RID1", "RID1", "RID2", "RID2", "RID1", "RID1", "RID2", "RID2"]
        ),
        ii,
    ]
)

idx.names = ["Item", "RID", "MP"]
df = DataFrame({"value": [1, 2, 3, 4, 5, 6, 7, 8]})
df.index = idx

query_df = DataFrame(
    {
        "Item": ["FC", "OWNER", "FC", "OWNER", "OWNER"],
        "RID": ["RID1", "RID1", "RID1", "RID2", "RID2"],
        "MP": [0.2, 1.5, 1.6, 11.1, 10.9],
    }
)

query_df = query_df.sort_index()

idx = pd.MultiIndex.from_arrays([query_df.Item, query_df.RID, query_df.MP])
query_df.index = idx
result = df.value.loc[query_df.index]

# the IntervalIndex level is indexed with floats, which map to
#  the intervals containing them.  Matching the behavior we would get
#  with _only_ an IntervalIndex, we get an IntervalIndex level back.
sliced_level = ii.take([0, 1, 1, 3, 2])
expected_index = pd.MultiIndex.from_arrays(
    [idx.get_level_values(0), idx.get_level_values(1), sliced_level]
)
expected = Series([1, 6, 2, 8, 7], index=expected_index, name="value")
tm.assert_series_equal(result, expected)
