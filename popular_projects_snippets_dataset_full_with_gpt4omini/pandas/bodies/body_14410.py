# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_keys.py

# GH 20523
# Puts a softlink into HDF file and rereads

with ensure_clean_store(setup_path) as store:

    df = DataFrame({"A": range(5), "B": range(5)})
    store.put("df", df)

    assert store.keys() == ["/df"]

    store._handle.create_soft_link(store._handle.root, "symlink", "df")

    # Should ignore the softlink
    assert store.keys() == ["/df"]
