# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py
# GH26610

df = DataFrame([1, 2, 3])
path = tmp_path / "empty_where.h5"
with HDFStore(path) as store:
    store.put("df", df, "t")
    result = read_hdf(store, "df", where=where)
    tm.assert_frame_equal(result, df)
