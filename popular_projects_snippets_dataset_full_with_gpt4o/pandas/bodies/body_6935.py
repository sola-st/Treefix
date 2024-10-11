# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_constructors.py
msg = "could not convert string to float"
with pytest.raises(ValueError, match=msg):
    Index(["a", "b", "c"], dtype=float)
