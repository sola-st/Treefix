# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_indexing.py
rows = {}
for date in data:
    for level in data[date]:
        rows[(date, level[0])] = {"A": level[1], "B": level[2]}

df = pd.DataFrame.from_dict(rows, orient="index")
df.index.names = ("Date", "Item")
exit(df)
