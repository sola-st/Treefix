# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
with pytest.raises(ValueError, match="Unrecognized compression type"):
    with tm.ensure_clean(get_random_path) as path:
        df = tm.makeDataFrame()
        df.to_pickle(path, compression=compression)
