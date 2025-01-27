# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_to_csv.py
# GH 8215
# Series.to_csv() was returning None, inconsistent with
# DataFrame.to_csv() which returned string
s = Series([1, 2, 3])
csv_str = s.to_csv(path_or_buf=None, header=False)
assert isinstance(csv_str, str)
