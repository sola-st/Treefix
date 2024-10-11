# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
with tm.ensure_clean("test.json") as path:
    s.to_json(path, encoding=encoding)
    retr = read_json(path, encoding=encoding)
    tm.assert_series_equal(s, retr, check_categorical=False)
