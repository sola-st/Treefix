# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
a = np.random.randint(0, 7, size=100)
b = np.random.randint(0, 3, size=100)
c = np.random.randint(0, 5, size=100)

df = DataFrame({"a": a, "b": b, "c": c})

result = crosstab(a, [b, c], rownames=["a"], colnames=("b", "c"), margins=True)

assert result.index.names == ("a",)
assert result.columns.names == ["b", "c"]

all_cols = result["All", ""]
exp_cols = df.groupby(["a"]).size().astype("i8")
# to keep index.name
exp_margin = Series([len(df)], index=Index(["All"], name="a"))
exp_cols = pd.concat([exp_cols, exp_margin])
exp_cols.name = ("All", "")

tm.assert_series_equal(all_cols, exp_cols)

all_rows = result.loc["All"]
exp_rows = df.groupby(["b", "c"]).size().astype("i8")
exp_rows = pd.concat([exp_rows, Series([len(df)], index=[("All", "")])])
exp_rows.name = "All"

exp_rows = exp_rows.reindex(all_rows.index)
exp_rows = exp_rows.fillna(0).astype(np.int64)
tm.assert_series_equal(all_rows, exp_rows)
