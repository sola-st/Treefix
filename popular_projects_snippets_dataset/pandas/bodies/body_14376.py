# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_subclass.py
data = {"a": [1, 2], "b": [3, 4]}
sdf = tm.SubclassedDataFrame(data, dtype=np.intp)

expected = DataFrame(data, dtype=np.intp)

path = tmp_path / "temp.h5"
sdf.to_hdf(path, "df")
result = read_hdf(path, "df")
tm.assert_frame_equal(result, expected)

path = tmp_path / "temp.h5"
with HDFStore(path) as store:
    store.put("df", sdf)
result = read_hdf(path, "df")
tm.assert_frame_equal(result, expected)
