# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# GH 43563
# explicit regex = True split
values = Series("xxxjpgzzz.jpg", dtype=any_string_dtype)
result = values.str.split(r"\.jpg", regex=True)
exp = Series([["xxxjpgzzz", ""]])
tm.assert_series_equal(result, exp)
