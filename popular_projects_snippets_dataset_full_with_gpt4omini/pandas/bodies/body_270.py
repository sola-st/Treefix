# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
mid = midhs
if parser == "python":
    ex1 = f"lhs {cmp1} mid {cmp2} rhs"
    msg = "'BoolOp' nodes are not implemented"
    with pytest.raises(NotImplementedError, match=msg):
        pd.eval(ex1, engine=engine, parser=parser)
    exit()

lhs_new = _eval_single_bin(lhs, cmp1, mid, engine)
rhs_new = _eval_single_bin(mid, cmp2, rhs, engine)

if lhs_new is not None and rhs_new is not None:
    ex1 = f"lhs {cmp1} mid {cmp2} rhs"
    ex2 = f"lhs {cmp1} mid and mid {cmp2} rhs"
    ex3 = f"(lhs {cmp1} mid) & (mid {cmp2} rhs)"
    expected = _eval_single_bin(lhs_new, "&", rhs_new, engine)

    for ex in (ex1, ex2, ex3):
        result = pd.eval(ex, engine=engine, parser=parser)

        tm.assert_almost_equal(result, expected)
