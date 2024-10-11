# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame([[0, 10], [1, 20]], columns=["cat", "count"])
expected = df[~(df.cat > 0)]

result = df.query("~(cat > 0)", engine=engine, parser=parser)
tm.assert_frame_equal(result, expected)

if parser == "python":
    msg = "'Not' nodes are not implemented"
    with pytest.raises(NotImplementedError, match=msg):
        df.query("not (cat > 0)", engine=engine, parser=parser)
else:
    result = df.query("not (cat > 0)", engine=engine, parser=parser)
    tm.assert_frame_equal(result, expected)
