# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_any_all.py
# GH#37506
data = [1.0, np.nan]
df = DataFrame(
    {"col1": pd.array(data, dtype=dtype1), "col2": pd.array(data, dtype=dtype2)}
)
result = df.groupby([1, 1]).agg("all", skipna=False)

expected = DataFrame({"col1": exp_col1, "col2": exp_col2}, index=np.array([1]))
tm.assert_frame_equal(result, expected)
