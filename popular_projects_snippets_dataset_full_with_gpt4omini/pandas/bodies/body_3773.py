# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_convert_dtypes.py
# Empty DataFrame can pass convert_dtypes, see GH#40393
empty_df = pd.DataFrame()
tm.assert_frame_equal(empty_df, empty_df.convert_dtypes())
