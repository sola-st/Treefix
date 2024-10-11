# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_dropna.py
# GH 3729
df_list = [
    ["A", "B", 12, 12, 12],
    ["A", None, 12.3, 233.0, 12],
    ["B", "A", 123.23, 123, 1],
    ["A", "B", 1, 1, 1.0],
]
df = pd.DataFrame(df_list, columns=["a", "b", "c", "d", "e"])
agg_dict = {"c": sum, "d": max, "e": "min"}
grouped = df.groupby(["a", "b"], dropna=dropna).agg(agg_dict)

mi = pd.MultiIndex.from_tuples(tuples, names=list("ab"))

# Since right now, by default MI will drop NA from levels when we create MI
# via `from_*`, so we need to add NA for level manually afterwards.
if not dropna:
    mi = mi.set_levels(["A", "B", np.nan], level="b")
expected = pd.DataFrame(outputs, index=mi)

tm.assert_frame_equal(grouped, expected)
