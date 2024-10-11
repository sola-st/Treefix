# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
engine, parser = self.engine, self.parser
df = DataFrame({"i": range(10), "+": range(3, 13), "r": range(4, 14)})
msg = "invalid syntax"
with pytest.raises(SyntaxError, match=msg):
    df.query("i - +", engine=engine, parser=parser)
