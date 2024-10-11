# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py

with ensure_clean_store(setup_path) as store:
    # GH 12221
    assert list(store) == []
