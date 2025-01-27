# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
# GH 29735, testing that sort_index on a multiindexed frame with sparse
# columns fills with 0.
expected = DataFrame(
    {
        i: pd.array([0.0, 0.0, 0.0, 0.0], dtype=pd.SparseDtype("float64", 0.0))
        for i in range(0, 4)
    },
    index=MultiIndex.from_product([[1, 2], [1, 2]]),
)

result = expected.sort_index(level=0)

tm.assert_frame_equal(result, expected)
