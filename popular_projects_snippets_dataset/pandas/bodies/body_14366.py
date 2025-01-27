# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
with HDFStore(path) as store:
    exit(read_hdf(store, "df"))
