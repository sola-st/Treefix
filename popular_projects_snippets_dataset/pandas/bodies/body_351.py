# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# xref https://github.com/pandas-dev/pandas/issues/12293
#  this fails on Windows, apparently a floating point precision issue

# Did not test complex64 because DataFrame is converting it to
# complex128. Due to https://github.com/pandas-dev/pandas/issues/10952
df = DataFrame({"a": np.random.randn(10).astype(dtype)})
assert df.a.dtype == dtype
df.eval("b = sin(a)", engine=engine, parser=parser, inplace=True)
got = df.b
expect = np.sin(df.a)
assert expect.dtype == got.dtype
assert expect_dtype == got.dtype
tm.assert_series_equal(got, expect, check_names=False)
