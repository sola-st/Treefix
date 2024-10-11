# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame(np.random.randn(5, 3))  # noqa:F841
ex = f"(df + 2)[df > 1] > 0 {char} (df > 0)"
if parser == "python":
    msg = "cannot evaluate scalar only bool ops"
    with pytest.raises(NotImplementedError, match=msg):
        pd.eval(ex, parser=parser, engine=engine)
else:
    # smoke-test, should not raise
    pd.eval(ex, parser=parser, engine=engine)
