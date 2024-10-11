# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
x, a, b = np.random.randn(3), 1, 2  # noqa:F841
df = DataFrame(np.random.randn(3, 2))  # noqa:F841

msg = "cannot evaluate scalar only bool ops|'BoolOp' nodes are not"
with pytest.raises(NotImplementedError, match=msg):
    pd.eval(ex, engine=engine, parser=parser)
