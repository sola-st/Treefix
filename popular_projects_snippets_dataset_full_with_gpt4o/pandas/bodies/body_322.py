# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame(np.random.randn(5, 2), columns=list("ab"))
# multiple assignment
df.eval("c = a + b", inplace=True)
msg = "can only assign a single expression"
with pytest.raises(SyntaxError, match=msg):
    df.eval("c = a = b")
