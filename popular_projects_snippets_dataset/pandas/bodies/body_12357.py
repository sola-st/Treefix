# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
df = DataFrame(np.zeros((1, 33000), dtype=np.int8))
with tm.ensure_clean() as path:
    with pytest.raises(ValueError, match="version must be either 118 or 119."):
        StataWriterUTF8(path, df, version=117)
with tm.ensure_clean() as path:
    with pytest.raises(ValueError, match="You must use version 119"):
        StataWriterUTF8(path, df, version=118)
