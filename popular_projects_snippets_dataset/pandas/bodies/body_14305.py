# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_file_handling.py

with ensure_clean_store(setup_path) as store:
    store["a"] = tm.makeTimeSeries()
    store.flush()
    store.flush(fsync=True)
