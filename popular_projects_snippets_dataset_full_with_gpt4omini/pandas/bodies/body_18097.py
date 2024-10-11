# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_series_equal.py
msg = """Series are different

Series values are different \\(66\\.66667 %\\)
\\[index\\]: \\[0, 1, 2\\]
\\[left\\]:  \\['a', 'b', 'c'\\]
Categories \\(3, object\\): \\['a', 'b', 'c'\\]
\\[right\\]: \\['a', 'c', 'b'\\]
Categories \\(3, object\\): \\['a', 'b', 'c'\\]"""

s1 = Series(Categorical(["a", "b", "c"]))
s2 = Series(Categorical(["a", "c", "b"]))

with pytest.raises(AssertionError, match=msg):
    tm.assert_series_equal(s1, s2, rtol=rtol)
