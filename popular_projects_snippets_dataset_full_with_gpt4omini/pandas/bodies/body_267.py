# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
if parser == "python" and binop in ["and", "or"]:
    msg = "'BoolOp' nodes are not implemented"
    with pytest.raises(NotImplementedError, match=msg):
        ex = f"(lhs {cmp1} rhs) {binop} (lhs {cmp2} rhs)"
        pd.eval(ex, engine=engine, parser=parser)
    exit()

lhs_new = _eval_single_bin(lhs, cmp1, rhs, engine)
rhs_new = _eval_single_bin(lhs, cmp2, rhs, engine)
expected = _eval_single_bin(lhs_new, binop, rhs_new, engine)

ex = f"(lhs {cmp1} rhs) {binop} (lhs {cmp2} rhs)"
result = pd.eval(ex, engine=engine, parser=parser)
tm.assert_equal(result, expected)
