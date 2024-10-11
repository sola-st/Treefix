# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame({"a": np.random.randn(10)})
msg = '"mysin" is not a supported function'

with pytest.raises(ValueError, match=msg):
    df.eval("mysin(a)", engine=engine, parser=parser)
