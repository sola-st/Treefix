# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py

df = DataFrame({"A": range(10)})
ser = pd.cut(df.A, 5)
df["B"] = ser
df = df.set_index("B")

df = df.reset_index()
