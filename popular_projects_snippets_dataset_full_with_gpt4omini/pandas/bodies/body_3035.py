# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_compare.py
# GH#30429
df = pd.DataFrame(
    {"col1": ["a", "b", "c"], "col2": [1.0, 2.0, np.nan], "col3": [1.0, 2.0, 3.0]},
    columns=["col1", "col2", "col3"],
)
df2 = df.copy()
df2.loc[0, "col1"] = "c"
df2.loc[2, "col3"] = 4.0

result = df.compare(df2, align_axis=align_axis)

if align_axis in (1, "columns"):
    indices = pd.Index([0, 2])
    columns = pd.MultiIndex.from_product([["col1", "col3"], ["self", "other"]])
    expected = pd.DataFrame(
        [["a", "c", np.nan, np.nan], [np.nan, np.nan, 3.0, 4.0]],
        index=indices,
        columns=columns,
    )
else:
    indices = pd.MultiIndex.from_product([[0, 2], ["self", "other"]])
    columns = pd.Index(["col1", "col3"])
    expected = pd.DataFrame(
        [["a", np.nan], ["c", np.nan], [np.nan, 3.0], [np.nan, 4.0]],
        index=indices,
        columns=columns,
    )
tm.assert_frame_equal(result, expected)
