# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH 26447
index = Index([str(x) for x in range(10)])
msg = "^'str' object cannot be interpreted as an integer$"
with pytest.raises(TypeError, match=msg):
    bytes(index)
