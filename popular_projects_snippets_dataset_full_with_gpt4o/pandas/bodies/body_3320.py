# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rank.py
dtype_na_map = {
    "float64": np.nan,
    "float32": np.nan,
    "object": None,
    "datetime64": np.datetime64("nat"),
}
# Insert nans at random positions if underlying dtype has missing
# value. Then adjust the expected order by adding nans accordingly
# This is for testing whether rank calculation is affected
# when values are interwined with nan values.
values = np.array(contents, dtype=dtype)
exp_order = np.array(range(len(values)), dtype="float64") + 1.0
if dtype in dtype_na_map:
    na_value = dtype_na_map[dtype]
    nan_indices = np.random.choice(range(len(values)), 5)
    values = np.insert(values, nan_indices, na_value)
    exp_order = np.insert(exp_order, nan_indices, np.nan)

# Shuffle the testing array and expected results in the same way
random_order = np.random.permutation(len(values))
obj = frame_or_series(values[random_order])
expected = frame_or_series(exp_order[random_order], dtype="float64")
result = obj.rank()
tm.assert_equal(result, expected)
