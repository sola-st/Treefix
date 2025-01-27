# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
e = "_var_s * 2"
tm.assert_numpy_array_equal(
    _var_s * 2, pd.eval(e, engine=engine, parser=parser)
)
