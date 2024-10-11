# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame(np.random.randn(5, 3), columns=list("abc"))
df2 = DataFrame(np.random.randn(5, 3))
expr1 = "df = df2"
msg = "cannot assign without a target object"
with pytest.raises(ValueError, match=msg):
    self.eval(expr1, local_dict={"df": df, "df2": df2})
