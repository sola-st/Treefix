# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
df = DataFrame(
    {
        "state": ["naive", "naive", "naive", "active", "active", "active"],
        "exp": ["a", "b", "b", "b", "a", "a"],
        "barcode": [1, 2, 3, 4, 1, 3],
        "v": ["hi", "hi", "bye", "bye", "bye", "peace"],
        "extra": np.arange(6.0),
    }
)

result = df.groupby(["state", "exp", "barcode", "v"]).apply(len)

unstacked = result.unstack()
restacked = unstacked.stack()
tm.assert_series_equal(restacked, result.reindex(restacked.index).astype(float))
