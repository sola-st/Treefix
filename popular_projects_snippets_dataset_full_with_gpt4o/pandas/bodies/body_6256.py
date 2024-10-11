# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
df = pd.DataFrame({"A": np.arange(len(data)), "B": data})
df.iloc[0, 1] = data[1]
assert df.loc[0, "B"] == data[1]
