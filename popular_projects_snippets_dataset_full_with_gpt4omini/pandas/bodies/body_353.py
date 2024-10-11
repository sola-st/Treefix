# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame({"a": np.random.randn(10)})
msg = 'Function "sin" does not support keyword arguments'

with pytest.raises(TypeError, match=msg):
    df.eval("sin(x=a)", engine=engine, parser=parser)
