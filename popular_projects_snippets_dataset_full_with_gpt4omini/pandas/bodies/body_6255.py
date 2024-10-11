# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
df = pd.DataFrame({"A": data, "B": data})
df.loc[10, "B"] = data[1]
assert df.loc[10, "B"] == data[1]
