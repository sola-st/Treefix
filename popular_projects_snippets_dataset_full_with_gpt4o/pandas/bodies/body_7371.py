# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_join.py
df = tm.makeCustomDataframe(
    10,
    10,
    data_gen_f=lambda *args, **kwargs: np.random.randn(),
    r_idx_type="i",
    c_idx_type="td",
)
str(df)

cols = df.columns.join(df.index, how="outer")
joined = cols.join(df.columns)
assert cols.dtype == np.dtype("O")
assert cols.dtype == joined.dtype
tm.assert_index_equal(cols, joined)
