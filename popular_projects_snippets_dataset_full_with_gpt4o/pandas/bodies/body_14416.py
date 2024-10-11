# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_complex.py
complex128 = np.array([1.0 + 1.0j, 1.0 + 1.0j, 1.0 + 1.0j, 1.0 + 1.0j])
s = Series(complex128, index=list("abcd"))
df = DataFrame({"A": s, "B": s})

with catch_warnings(record=True):

    objs = [df]
    comps = [tm.assert_frame_equal]
    for obj, comp in zip(objs, comps):
        path = tmp_path / setup_path
        obj.to_hdf(path, "obj", format="table")
        reread = read_hdf(path, "obj")
        comp(obj, reread)
