# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
df = DataFrame({"a": [1, 2], "b": ["c", "d"]})
msg = r"unsupported operand type\(s\) for .+: '.+' and '.+'"

with pytest.raises(TypeError, match=msg):
    df.eval(f"a {op} b", engine=engine, parser=parser)
