# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_errors.py
df = DataFrame(np.random.randn(10, 1))
df2 = DataFrame({"a": np.random.randn(10)})
df3 = DataFrame({(1, 2): np.random.randn(10)})
df4 = DataFrame({("1", 2): np.random.randn(10)})
df5 = DataFrame({("1", 2, object): np.random.randn(10)})

with ensure_clean_store(setup_path) as store:
    name = f"df_{tm.rands(10)}"
    store.append(name, df)

    for d in (df2, df3, df4, df5):
        msg = re.escape(
            "cannot match existing table structure for [0] on appending data"
        )
        with pytest.raises(ValueError, match=msg):
            store.append(name, d)
