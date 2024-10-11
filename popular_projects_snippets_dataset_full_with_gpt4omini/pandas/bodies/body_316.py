# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame(np.random.randn(5, 2), columns=list("ab"))
# invalid assignees
msg = "left hand side of an assignment must be a single name"
with pytest.raises(SyntaxError, match=msg):
    df.eval("d,c = a + b")
