# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
# GH50085
original = data.copy()
df = pd.DataFrame({"a": data, "b": data})
df.loc[[0, 1], :] = df.loc[[1, 0], :].values
assert (df.loc[0, :] == original[1]).all()
assert (df.loc[1, :] == original[0]).all()
