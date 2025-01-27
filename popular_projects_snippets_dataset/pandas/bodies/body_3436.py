# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
dr = date_range("2012-06-02", periods=10, tz=tz)
df = DataFrame(np.random.randn(len(dr)), dr)
roundtripped = df.reset_index().set_index("index")
xp = df.index.tz
rs = roundtripped.index.tz
assert xp == rs
