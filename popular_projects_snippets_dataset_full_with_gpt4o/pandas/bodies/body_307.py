# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
ex = f"{lhs} {op} {rhs}"

if parser == "python" and op in ["and", "or"]:
    msg = "'BoolOp' nodes are not implemented"
    with pytest.raises(NotImplementedError, match=msg):
        self.eval(ex)
    exit()

res = self.eval(ex)
exp = eval(ex)
assert res == exp
