# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_indexing.py
# https://github.com/pandas-dev/pandas/issues/34191

msg = "Indexing with a float is no longer supported"
with pytest.raises(IndexError, match=msg):
    idx[1.0]
