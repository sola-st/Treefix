# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_almost_equal.py
msg = """Iterable are different

Iterable length are different
\\[left\\]:  2
\\[right\\]: 3"""

with pytest.raises(AssertionError, match=msg):
    tm.assert_almost_equal([1, 2], [3, 4, 5])
