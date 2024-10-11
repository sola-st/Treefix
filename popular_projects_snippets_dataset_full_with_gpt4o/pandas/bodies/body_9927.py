# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py

df = DataFrame({"B": [0, 1, 2, np.nan, 4]})
df
df.expanding(2).sum()
