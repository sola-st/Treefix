# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 17013

df = data.copy()
df[["D", "E", "F"]] = np.arange(len(df) * 3).reshape(len(df), 3).astype("i8")

mi_val = list(product(["bar", "foo"], ["one", "two"])) + [("All", "")]
mi = MultiIndex.from_tuples(mi_val, names=("A", "B"))
expected = DataFrame(
    {"dull": [12, 21, 3, 9, 45], "shiny": [33, 0, 36, 51, 120]}, index=mi
).rename_axis("C", axis=1)
expected["All"] = expected["dull"] + expected["shiny"]

result = df.pivot_table(
    values="D",
    index=["A", "B"],
    columns="C",
    margins=True,
    aggfunc=np.sum,
    fill_value=0,
)

tm.assert_frame_equal(expected, result)
