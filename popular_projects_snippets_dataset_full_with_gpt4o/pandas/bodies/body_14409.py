# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_keys.py
with ensure_clean_store(setup_path) as store:
    with pytest.raises(
        ValueError,
        match="`include` should be either 'pandas' or 'native' but is 'illegal'",
    ):
        store.keys(include="illegal")
