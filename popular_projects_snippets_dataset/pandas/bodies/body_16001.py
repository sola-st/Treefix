# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_isin.py
s = Series(["A", "B", "C", "a", "B", "B", "A", "C"])

result = s.isin(["A", "C"])
expected = Series([True, False, True, False, False, False, True, True])
tm.assert_series_equal(result, expected)

# GH#16012
# This specific issue has to have a series over 1e6 in len, but the
# comparison array (in_list) must be large enough so that numpy doesn't
# do a manual masking trick that will avoid this issue altogether
s = Series(list("abcdefghijk" * 10**5))
# If numpy doesn't do the manual comparison/mask, these
# unorderable mixed types are what cause the exception in numpy
in_list = [-1, "a", "b", "G", "Y", "Z", "E", "K", "E", "S", "I", "R", "R"] * 6

assert s.isin(in_list).sum() == 200000
