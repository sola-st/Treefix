# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py

df = DataFrame({"B": [0, 1, 2, np.nan, 4]})
df
df.ewm(com=0.5).mean()
