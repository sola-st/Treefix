# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# keep the `d` category with 0
s = Series(Categorical(list("bbbaac"), categories=list("abcd"), ordered=True))
result = s.value_counts()
expected = Series(
    [3, 2, 1, 0],
    index=Categorical(
        ["b", "a", "c", "d"], categories=list("abcd"), ordered=True
    ),
)
tm.assert_series_equal(result, expected, check_index_type=True)
