# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_indexing.py
with pytest.raises(IndexError, match="bounds"):
    arr.take([11])
