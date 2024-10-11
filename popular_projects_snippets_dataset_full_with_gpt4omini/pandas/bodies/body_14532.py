# Extracted from ./data/repos/pandas/pandas/tests/io/test_feather.py
# GH 29055
url = (
    "https://raw.githubusercontent.com/pandas-dev/pandas/main/"
    "pandas/tests/io/data/feather/feather-0_3_1.feather"
)
expected = read_feather(feather_file)
res = read_feather(url)
tm.assert_frame_equal(expected, res)
