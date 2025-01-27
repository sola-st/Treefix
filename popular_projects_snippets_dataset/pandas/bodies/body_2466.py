# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#47687
midx = MultiIndex.from_arrays(
    [
        Series([True, True, False, False], dtype=dtype),
        Series([True, False, True, False], dtype=dtype),
    ],
    names=["a", "b"],
)
df = DataFrame({"c": [1, 2, 3, 4]}, index=midx)
with tm.maybe_produces_warning(PerformanceWarning, isinstance(indexer, tuple)):
    result = df.loc[indexer]
expected = DataFrame(
    {"c": [1, 2]}, index=Index([True, False], name="b", dtype=dtype)
)
tm.assert_frame_equal(result, expected)
