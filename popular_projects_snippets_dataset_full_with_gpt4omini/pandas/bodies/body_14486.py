# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_errors.py

df = tm.makeDataFrame()

with ensure_clean_store(setup_path) as store:
    store.put("df", df)
    msg = (
        "cannot pass a column specification when reading a Fixed format "
        "store. this store must be selected in its entirety"
    )
    with pytest.raises(TypeError, match=msg):
        store.select("df", columns=["A"])
    msg = (
        "cannot pass a where specification when reading from a Fixed "
        "format store. this store must be selected in its entirety"
    )
    with pytest.raises(TypeError, match=msg):
        store.select("df", where=[("columns=A")])
