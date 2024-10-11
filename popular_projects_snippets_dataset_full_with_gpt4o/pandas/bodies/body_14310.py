# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_file_handling.py
enc = "latin-1"
nan_rep = ""
key = "data"

val = [x.decode(enc) if isinstance(x, bytes) else x for x in val]
ser = Series(val, dtype=dtype)

store = tmp_path / setup_path
ser.to_hdf(store, key, format="table", encoding=enc, nan_rep=nan_rep)
retr = read_hdf(store, key)

s_nan = ser.replace(nan_rep, np.nan)

tm.assert_series_equal(s_nan, retr)
