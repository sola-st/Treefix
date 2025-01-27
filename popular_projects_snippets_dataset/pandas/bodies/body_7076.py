# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_any_index.py
if not len(index):
    exit()
msg = "Index does not support mutable operations"
with pytest.raises(TypeError, match=msg):
    index[0] = index[0]
