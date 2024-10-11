# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
df = DataFrame(np.random.randn(5, 3))

# can't reference ourself b/c we're a local so @ is necessary
with pytest.raises(UndefinedVariableError, match="name 'df' is not defined"):
    df.query("df > 0", engine=self.engine, parser=self.parser)
