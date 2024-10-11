# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
columns = ["x", "y"]
original = DataFrame(np.reshape(np.arange(10.0), (5, 2)), columns=columns)
original.index.name = "index_not_written"
with tm.ensure_clean() as path:
    original.to_stata(path, write_index=False)
    written_and_read_again = self.read_dta(path)
    with pytest.raises(KeyError, match=original.index.name):
        written_and_read_again["index_not_written"]
