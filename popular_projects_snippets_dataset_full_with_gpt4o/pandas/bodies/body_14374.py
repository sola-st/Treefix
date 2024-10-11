# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
# GH22073
df = DataFrame({"a": [1, 2, 3, 4], "b": [5, 6, 7, 8]})
with ensure_clean_store(setup_path) as store:
    store.put("df", df)
    assert df["a"].values.strides == store["df"]["a"].values.strides
