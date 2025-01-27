# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# https://github.com/pandas-dev/pandas/issues/35286
df = DataFrame(
    {"A": [0, 1], "B": pd.array([0, 1], dtype=pd.SparseDtype("int64", 0))}
)
result = df.reindex([0, 2])
expected = DataFrame(
    {
        "A": [0.0, np.nan],
        "B": pd.array([0.0, np.nan], dtype=pd.SparseDtype("float64", 0.0)),
    },
    index=[0, 2],
)
tm.assert_frame_equal(result, expected)
