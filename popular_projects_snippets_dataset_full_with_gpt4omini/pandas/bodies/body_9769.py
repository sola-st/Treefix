# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
df = DataFrame({"A": np.arange(5)})
roll = df.rolling(2, win_type="triang")

msg = f"'{arg}' is not a valid function for 'Window' object"
with pytest.raises(AttributeError, match=msg):
    roll.agg(arg)

with pytest.raises(AttributeError, match=msg):
    roll.agg([arg])

with pytest.raises(AttributeError, match=msg):
    roll.agg({"A": arg})
