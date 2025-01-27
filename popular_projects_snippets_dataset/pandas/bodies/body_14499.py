# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_pytables_missing.py
df = pd.DataFrame({"A": [1, 2]})
with pytest.raises(ImportError, match="tables"):
    with tm.ensure_clean("foo.h5") as path:
        df.to_hdf(path, "df")
