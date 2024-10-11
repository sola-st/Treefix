# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: setting values with a row indexer on a viewing subset
# subset[indexer] = value and subset.iloc[indexer] = value
df = DataFrame({"a": [1, 2, 3, 4], "b": [4, 5, 6, 7], "c": [0.1, 0.2, 0.3, 0.4]})
df_orig = df.copy()
subset = df[1:4]

if (
    indexer_si is tm.setitem
    and isinstance(indexer, np.ndarray)
    and indexer.dtype == "int"
):
    pytest.skip("setitem with labels selects on columns")

if using_copy_on_write:
    indexer_si(subset)[indexer] = 0
else:
    # INFO iloc no longer raises warning since pandas 1.4
    warn = SettingWithCopyWarning if indexer_si is tm.setitem else None
    with pd.option_context("chained_assignment", "warn"):
        with tm.assert_produces_warning(warn):
            indexer_si(subset)[indexer] = 0

expected = DataFrame(
    {"a": [0, 0, 4], "b": [0, 0, 7], "c": [0.0, 0.0, 0.4]}, index=range(1, 4)
)
tm.assert_frame_equal(subset, expected)
if using_copy_on_write:
    # original parent dataframe is not modified (CoW)
    tm.assert_frame_equal(df, df_orig)
else:
    # original parent dataframe is actually updated
    df_orig[1:3] = 0
    tm.assert_frame_equal(df, df_orig)
