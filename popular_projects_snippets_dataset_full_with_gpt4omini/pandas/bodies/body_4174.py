# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
from pandas.errors import NumExprClobberingError

engine, parser = self.engine, self.parser

n = m = 10
df = DataFrame(np.random.randint(m, size=(n, 3)), columns=list("abc"))

df.index.name = "sin"
msg = "Variables in expression.+"
with pytest.raises(NumExprClobberingError, match=msg):
    df.query("sin > 5", engine=engine, parser=parser)
