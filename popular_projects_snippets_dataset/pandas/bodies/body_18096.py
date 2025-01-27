# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_series_equal.py
msg = """Series are different

Series values are different \\(33\\.33333 %\\)
\\[index\\]: \\[0, 1, 2\\]
\\[left\\]:  \\[1, 2, 3\\]
\\[right\\]: \\[1, 2, 4\\]"""

s1 = Series([1, 2, 3])
s2 = Series([1, 2, 4])

with pytest.raises(AssertionError, match=msg):
    tm.assert_series_equal(s1, s2, rtol=rtol)
