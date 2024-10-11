# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py

nan_df1 = DataFrame(np.random.rand(10, 5))
nan_df1[nan_df1 > 0.5] = np.nan

opts = (
    DataFrame(np.random.randn(10, 5)),
    Series(np.random.randn(5)),
    Series([1, 2, np.nan, np.nan, 5]),
    nan_df1,
    np.random.randn(),
)
exit(opts[request.param])
