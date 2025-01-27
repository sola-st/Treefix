# Extracted from ./data/repos/pandas/pandas/tests/io/test_fsspec.py
tm.assert_equal(
    read_csv(f"{protocol}://pandas-test/tips.csv", storage_options=s3so),
    read_csv(tips_file),
)
