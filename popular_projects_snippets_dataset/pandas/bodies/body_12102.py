# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_network.py
# GH 29055
expected = read_feather(feather_file)
res = read_feather(
    "s3://pandas-test/simple_dataset.feather", storage_options=s3so
)
tm.assert_frame_equal(expected, res)
