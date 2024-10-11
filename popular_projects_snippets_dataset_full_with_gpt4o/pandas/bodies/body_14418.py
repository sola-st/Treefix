# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_complex.py
complex128 = np.array([1.0 + 1.0j, 1.0 + 1.0j, 1.0 + 1.0j, 1.0 + 1.0j])
s = Series(complex128, index=list("abcd"))

msg = (
    "Columns containing complex values can be stored "
    "but cannot be indexed when using table format. "
    "Either use fixed format, set index=False, "
    "or do not include the columns containing complex "
    "values to data_columns when initializing the table."
)

path = tmp_path / setup_path
with pytest.raises(TypeError, match=msg):
    s.to_hdf(path, "obj", format="t")

path = tmp_path / setup_path
s.to_hdf(path, "obj", format="t", index=False)
reread = read_hdf(path, "obj")
tm.assert_series_equal(s, reread)
