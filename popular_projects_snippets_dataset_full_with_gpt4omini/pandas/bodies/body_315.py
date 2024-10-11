# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame(np.random.randn(5, 2), columns=list("ab"))
# multiple assignees
with pytest.raises(SyntaxError, match="invalid syntax"):
    df.eval("d c = a + b")
