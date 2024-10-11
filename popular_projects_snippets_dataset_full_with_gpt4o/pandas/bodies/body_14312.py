# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_file_handling.py
with tm.ensure_clean("foo.h5") as path:
    with HDFStore(path) as store:
        assert os.fspath(store) == str(path)
