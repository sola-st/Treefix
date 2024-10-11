# Extracted from ./data/repos/pandas/pandas/tests/io/test_fsspec.py
msg = "Missing optional dependency 'fsspec'|fsspec library is required"
with pytest.raises(ImportError, match=msg):
    read_csv("memory://test/test.csv")
