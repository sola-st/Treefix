# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_value_counts.py
df = pd.DataFrame({"num_legs": [2, 4, 4, 6]})

result = df.value_counts()
expected = pd.Series(
    data=[2, 1, 1],
    index=pd.MultiIndex.from_arrays([[4, 2, 6]], names=["num_legs"]),
)

tm.assert_series_equal(result, expected)
