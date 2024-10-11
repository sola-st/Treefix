# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# odd failure on win32 platform, so skip
ex = "lhs ** rhs"
expected = _eval_single_bin(lhs, "**", rhs, engine)
result = pd.eval(ex, engine=engine, parser=parser)

if (
    is_scalar(lhs)
    and is_scalar(rhs)
    and isinstance(expected, (complex, np.complexfloating))
    and np.isnan(result)
):
    msg = "(DataFrame.columns|numpy array) are different"
    with pytest.raises(AssertionError, match=msg):
        tm.assert_numpy_array_equal(result, expected)
else:
    tm.assert_almost_equal(result, expected)

    ex = "(lhs ** rhs) ** rhs"
    result = pd.eval(ex, engine=engine, parser=parser)

    middle = _eval_single_bin(lhs, "**", rhs, engine)
    expected = _eval_single_bin(middle, "**", rhs, engine)
    tm.assert_almost_equal(result, expected)
