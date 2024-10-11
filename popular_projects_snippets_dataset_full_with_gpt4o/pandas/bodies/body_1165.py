# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_multiindex.py
# GH19414
tm.assert_series_equal(
    Series([1, 2], MultiIndex.from_arrays([["a", "b"]])).loc[
        ["a", "a", "b", "b"]
    ],
    Series([1, 1, 2, 2], MultiIndex.from_arrays([["a", "a", "b", "b"]])),
)
