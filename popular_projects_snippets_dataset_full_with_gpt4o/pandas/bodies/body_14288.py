# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py

with ensure_clean_store(setup_path) as store:

    # with all empty strings (GH 12242)
    df = DataFrame({"x": ["a", "b", "c", "d", "e", "f", ""]})
    store.append("df", df[:-1], min_itemsize={"x": 1})
    store.append("df", df[-1:], min_itemsize={"x": 1})
    tm.assert_frame_equal(store.select("df"), df)
