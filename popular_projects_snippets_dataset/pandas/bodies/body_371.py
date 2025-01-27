# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
gen = {int: lambda: np.random.randint(10), float: np.random.randn}

mid = gen[lhs]()  # noqa:F841
lhs = gen[lhs]()
rhs = gen[rhs]()

ex1 = f"lhs {cmp} mid {cmp} rhs"
ex2 = f"lhs {cmp} mid and mid {cmp} rhs"
ex3 = f"(lhs {cmp} mid) & (mid {cmp} rhs)"
for ex in (ex1, ex2, ex3):
    msg = "cannot evaluate scalar only bool ops|'BoolOp' nodes are not"
    with pytest.raises(NotImplementedError, match=msg):
        pd.eval(ex, engine=engine, parser=parser)
