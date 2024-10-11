# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# re.split 0, str.split -1
s = Series(data, dtype=any_string_dtype)

result = s.str.split(pat=pat, n=n)
xp = s.str.split(pat=pat)
tm.assert_series_equal(result, xp)
