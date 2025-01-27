# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_cython.py
frame = DataFrame(
    {
        "a": np.random.randint(0, 5, 50),
        "b": np.random.randint(0, 2, 50).astype("bool"),
    }
)
result = frame.groupby("a")["b"].mean()
expected = frame.groupby("a")["b"].agg(np.mean)

tm.assert_series_equal(result, expected)
