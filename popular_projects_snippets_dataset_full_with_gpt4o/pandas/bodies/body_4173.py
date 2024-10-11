# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
engine, parser = self.engine, self.parser
n = m = 10
df = DataFrame(np.random.randint(m, size=(n, 3)), columns=list("abc"))

# we don't pick up the local 'sin'
with pytest.raises(UndefinedVariableError, match="name 'sin' is not defined"):
    df.query("sin > 5", engine=engine, parser=parser)
