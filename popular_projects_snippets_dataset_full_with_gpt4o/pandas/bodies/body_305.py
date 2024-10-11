# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
exclude_arith = []
if parser == "python":
    exclude_arith = ["in", "not in"]

arith_ops = [
    op
    for op in expr.ARITH_OPS_SYMS + expr.CMP_OPS_SYMS
    if op not in exclude_arith
]

ops = (op for op in arith_ops if op != "//")

for op in ops:
    ex = f"1 {op} 1"
    ex2 = f"x {op} 1"
    ex3 = f"1 {op} (x + 1)"

    if op in ("in", "not in"):
        msg = "argument of type 'int' is not iterable"
        with pytest.raises(TypeError, match=msg):
            pd.eval(ex, engine=engine, parser=parser)
    else:
        expec = _eval_single_bin(1, op, 1, engine)
        x = self.eval(ex, engine=engine, parser=parser)
        assert x == expec

        expec = _eval_single_bin(x, op, 1, engine)
        y = self.eval(ex2, local_dict={"x": x}, engine=engine, parser=parser)
        assert y == expec

        expec = _eval_single_bin(1, op, x + 1, engine)
        y = self.eval(ex3, local_dict={"x": x}, engine=engine, parser=parser)
        assert y == expec
