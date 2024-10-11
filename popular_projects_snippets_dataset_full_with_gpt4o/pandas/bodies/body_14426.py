# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_put.py
df = DataFrame({"A": [1, 2]})
with HDFStore(tmp_path / setup_path) as store:
    store.put("a", df, format="fixed")
    store.put("b", df, format="table")

    assert store.get_storer("a").format_type == "fixed"
    assert store.get_storer("b").format_type == "table"
