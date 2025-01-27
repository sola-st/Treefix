# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_join.py
df = tm.makeCustomDataframe(
    10,
    10,
    data_gen_f=lambda *args, **kwargs: np.random.randn(),
    r_idx_type="i",
    c_idx_type="dt",
)
cols = df.columns.join(df.index, how="outer")
joined = cols.join(df.columns)
assert cols.dtype == np.dtype("O")
assert cols.dtype == joined.dtype
tm.assert_numpy_array_equal(cols.values, joined.values)
