# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_index_equal.py
idx1 = Index([1, 2, 3.0])
idx2 = Index([1, 2, 3.0001])
kwargs = {"check_exact": check_exact, "rtol": rtol}

if check_exact or rtol < 0.5e-3:
    msg = """Index are different

Index values are different \\(33\\.33333 %\\)
\\[left\\]:  NumericIndex\\(\\[1.0, 2.0, 3.0], dtype='float64'\\)
\\[right\\]: NumericIndex\\(\\[1.0, 2.0, 3.0001\\], dtype='float64'\\)"""

    with pytest.raises(AssertionError, match=msg):
        tm.assert_index_equal(idx1, idx2, **kwargs)
else:
    tm.assert_index_equal(idx1, idx2, **kwargs)
