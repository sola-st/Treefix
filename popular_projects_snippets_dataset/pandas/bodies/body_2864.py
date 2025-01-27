# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# don't try to fill boolean, int blocks

df = DataFrame(np.random.randn(10, 4).astype(int))

# it works!
df.fillna(np.nan)
