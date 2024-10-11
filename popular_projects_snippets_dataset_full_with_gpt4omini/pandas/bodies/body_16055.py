# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_convert_dtypes.py
# GH32287
df = pd.DataFrame({"A": pd.array([True])})
tm.assert_frame_equal(df, df.convert_dtypes())
