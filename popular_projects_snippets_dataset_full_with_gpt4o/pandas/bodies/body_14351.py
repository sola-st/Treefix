# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
# GH #13492
idx = Index(
    pd.to_datetime([dt.date(2000, 1, 1), dt.date(2000, 1, 2)]),
    name="cols\u05d2",
)
idx1 = Index(
    pd.to_datetime([dt.date(2010, 1, 1), dt.date(2010, 1, 2)]),
    name="rows\u05d0",
)
df = DataFrame(np.arange(4).reshape(2, 2), columns=idx, index=idx1)

# This used to fail, returning numpy strings instead of python strings.
path = tmp_path / setup_path
df.to_hdf(path, "df", format=table_format)
df2 = read_hdf(path, "df")

tm.assert_frame_equal(df, df2, check_names=True)

assert type(df2.index.name) == str
assert type(df2.columns.name) == str
