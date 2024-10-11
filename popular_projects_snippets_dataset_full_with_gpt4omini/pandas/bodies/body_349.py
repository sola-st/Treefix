# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame({"a": np.random.randn(10), "b": np.random.randn(10)})
df.eval(
    "e = arctan2(sin(a), b)",
    engine=engine,
    parser=parser,
    inplace=True,
)
got = df.e
expect = np.arctan2(np.sin(df.a), df.b)
tm.assert_series_equal(got, expect, check_names=False)
