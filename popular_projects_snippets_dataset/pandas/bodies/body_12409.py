# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
# Same test as write_fspath_all, except HDF5 files aren't
# necessarily byte-for-byte identical for a given dataframe, so we'll
# have to read and compare equality
pytest.importorskip("tables")

df = pd.DataFrame({"A": [1, 2]})
p1 = tm.ensure_clean("string")
p2 = tm.ensure_clean("fspath")

with p1 as string, p2 as fspath:
    mypath = CustomFSPath(fspath)
    df.to_hdf(mypath, key="bar")
    df.to_hdf(string, key="bar")

    result = pd.read_hdf(fspath, key="bar")
    expected = pd.read_hdf(string, key="bar")

tm.assert_frame_equal(result, expected)
