# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_network.py
# Read from AWS s3 as "s3a" URL
df = read_csv("s3a://pandas-test/tips.csv", nrows=10, storage_options=s3so)
assert isinstance(df, DataFrame)
assert not df.empty
tm.assert_frame_equal(tips_df.iloc[:10], df)
