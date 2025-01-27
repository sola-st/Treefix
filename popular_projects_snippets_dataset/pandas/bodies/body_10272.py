# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_dropna.py
# GH 36604
df = pd.DataFrame({"A": [0, 0, 1, None], "B": [1, 2, 3, None]})
gb = df.groupby("A", dropna=dropna)
assert gb.grouper.dropna == dropna
