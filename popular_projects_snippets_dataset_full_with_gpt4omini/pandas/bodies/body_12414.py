# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
"""
        'encoding' shouldn't be passed to 'open' in binary mode.

        GH 35058
        """
with tm.ensure_clean() as path:
    df = tm.makeDataFrame()
    df.to_csv(path, mode="w+b")
    tm.assert_frame_equal(df, pd.read_csv(path, index_col=0))
