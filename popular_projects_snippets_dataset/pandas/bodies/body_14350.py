# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
df = tm.makeDataFrame()
df.index.name = "foo"

with ensure_clean_store(setup_path) as store:
    store["frame"] = df
    recons = store["frame"]
    tm.assert_frame_equal(recons, df)
