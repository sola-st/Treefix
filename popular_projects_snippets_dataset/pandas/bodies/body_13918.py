# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
"""
        Binary file objects should work (if 'mode' contains a 'b') or even without
        it in most cases.

        GH 35058 and GH 19827
        """
df = tm.makeDataFrame()
with tm.ensure_clean() as path:
    with open(path, mode="w+b") as handle:
        df.to_csv(handle, mode=mode)
    tm.assert_frame_equal(df, pd.read_csv(path, index_col=0))
