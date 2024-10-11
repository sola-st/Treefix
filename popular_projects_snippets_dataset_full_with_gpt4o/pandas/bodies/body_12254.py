# Extracted from ./data/repos/pandas/pandas/tests/io/test_fsspec.py
tm.assert_equal(
    read_csv("s3://pandas-test/tips.csv", storage_options=s3so), read_csv(tips_file)
)
# the following are decompressed by pandas, not fsspec
tm.assert_equal(
    read_csv("s3://pandas-test/tips.csv.gz", storage_options=s3so),
    read_csv(tips_file),
)
tm.assert_equal(
    read_csv("s3://pandas-test/tips.csv.bz2", storage_options=s3so),
    read_csv(tips_file),
)
