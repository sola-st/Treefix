# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_value_counts.py
df = pd.DataFrame(
    {"num_legs": [2, 4, 4, 6], "num_wings": [2, 0, 0, 0]},
    index=["falcon", "dog", "cat", "ant"],
)

result = df.value_counts(sort=False)
expected = pd.Series(
    data=[1, 2, 1],
    index=pd.MultiIndex.from_arrays(
        [(2, 4, 6), (2, 0, 0)], names=["num_legs", "num_wings"]
    ),
)

tm.assert_series_equal(result, expected)
