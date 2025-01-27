# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame(np.random.randn(5, 2), columns=list("ab"))
msg = "cannot assign to function call"
with pytest.raises(SyntaxError, match=msg):
    df.eval('Timestamp("20131001") = a + b')
