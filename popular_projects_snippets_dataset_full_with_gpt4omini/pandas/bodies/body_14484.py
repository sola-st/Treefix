# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_read.py
# GH 16583
# Tests that reading a Series saved to an HDF file
# still works if a mode='r' argument is supplied
series = tm.makeFloatSeries()
path = tmp_path / setup_path
series.to_hdf(path, key="data", format=format)
result = read_hdf(path, key="data", mode="r")
tm.assert_series_equal(result, series)
