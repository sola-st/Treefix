# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_complex.py
with catch_warnings(record=True):
    complex128 = np.array([1.0 + 1.0j, 1.0 + 1.0j, 1.0 + 1.0j, 1.0 + 1.0j])
    s = Series(complex128, index=list("abcd"))
    df = DataFrame({"A": s, "B": s})

    objs = [s, df]
    comps = [tm.assert_series_equal, tm.assert_frame_equal]
    for obj, comp in zip(objs, comps):
        path = tmp_path / setup_path
        obj.to_hdf(path, "obj", format="fixed")
        reread = read_hdf(path, "obj")
        comp(obj, reread)
