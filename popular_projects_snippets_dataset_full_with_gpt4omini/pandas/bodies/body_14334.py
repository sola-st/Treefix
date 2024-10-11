# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py

with ensure_clean_store(setup_path) as store:
    store["a"] = tm.makeTimeSeries()
    store["b"] = tm.makeDataFrame()
    store["foo/bar"] = tm.makeDataFrame()
    assert "a" in store
    assert "b" in store
    assert "c" not in store
    assert "foo/bar" in store
    assert "/foo/bar" in store
    assert "/foo/b" not in store
    assert "bar" not in store

    # gh-2694: tables.NaturalNameWarning
    with catch_warnings(record=True):
        store["node())"] = tm.makeDataFrame()
    assert "node())" in store
