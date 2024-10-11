# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_network.py
# GH 25945
result = read_csv("s3://pandas-test/tips#1.csv", storage_options=s3so)
tm.assert_frame_equal(tips_df, result)
