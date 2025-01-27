# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_complex.py
complex64 = np.array(
    [1.0 + 1.0j, 1.0 + 1.0j, 1.0 + 1.0j, 1.0 + 1.0j], dtype=np.complex64
)
complex128 = np.array(
    [1.0 + 1.0j, 1.0 + 1.0j, 1.0 + 1.0j, 1.0 + 1.0j], dtype=np.complex128
)
df = DataFrame(
    {
        "A": [1, 2, 3, 4],
        "B": ["a", "b", "c", "d"],
        "C": complex64,
        "D": complex128,
        "E": [1.0, 2.0, 3.0, 4.0],
    },
    index=list("abcd"),
)

with ensure_clean_store(setup_path) as store:
    store.append("df", df, data_columns=["A", "B"])
    result = store.select("df", where="A>2")
    tm.assert_frame_equal(df.loc[df.A > 2], result)

path = tmp_path / setup_path
df.to_hdf(path, "df", format="table")
reread = read_hdf(path, "df")
tm.assert_frame_equal(df, reread)
