# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 18221
df = DataFrame([[0, 0, 0]], columns=["foo", "bar", "class"])
msg = "Python keyword not valid identifier in numexpr query"
with pytest.raises(SyntaxError, match=msg):
    df.query("class == 0")

df = DataFrame()
df.index.name = "lambda"
with pytest.raises(SyntaxError, match=msg):
    df.query("lambda == 0")
