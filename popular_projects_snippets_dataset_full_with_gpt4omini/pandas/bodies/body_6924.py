# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_reshape.py
index = Index(["a", "b", "c", "d"], name="index")
msg = "index 5 is out of bounds for axis 0 with size 4"
with pytest.raises(IndexError, match=msg):
    index.delete(5)
