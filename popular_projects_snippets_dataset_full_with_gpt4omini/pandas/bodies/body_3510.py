# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_update.py
df = DataFrame([[1.5, 1, 3.0]])
with pytest.raises(exception, match=msg):
    df.update(df, **bad_kwarg)
