# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
# groupby example
NUM_ROWS = 100
NUM_COLS = 10
col_names = ["A" + num for num in map(str, np.arange(NUM_COLS).tolist())]
index_cols = col_names[:5]

df = DataFrame(
    np.random.randint(5, size=(NUM_ROWS, NUM_COLS)),
    dtype=np.int64,
    columns=col_names,
)
df = df.set_index(index_cols).sort_index()
grp = df.groupby(level=index_cols[:4])
df["new_col"] = np.nan

# we are actually operating on a copy here
# but in this case, that's ok
for name, df2 in grp:
    new_vals = np.arange(df2.shape[0])
    df.loc[name, "new_col"] = new_vals
