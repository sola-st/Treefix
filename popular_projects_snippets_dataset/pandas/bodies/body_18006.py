# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_almost_equal.py

msg = f"""numpy array are different

numpy array classes are different
\\[left\\]:  {klass1}
\\[right\\]: {klass2}"""

with pytest.raises(AssertionError, match=msg):
    tm.assert_almost_equal(a, b)
