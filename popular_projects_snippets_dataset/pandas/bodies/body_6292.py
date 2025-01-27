# Extracted from ./data/repos/pandas/pandas/tests/extension/base/groupby.py
df = pd.DataFrame(
    {"A": ["B", "B", None, None, "A", "A", "B", "C"], "B": data_for_grouping}
)
gr1 = df.groupby("A").grouper.groupings[0]
gr2 = df.groupby("B").grouper.groupings[0]

tm.assert_numpy_array_equal(gr1.grouping_vector, df.A.values)
tm.assert_extension_array_equal(gr2.grouping_vector, data_for_grouping)
