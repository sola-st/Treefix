# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 19342
# construction with single-element container and index
# should raise
msg = r"Length of values \(1\) does not match length of index \(3\)"
with pytest.raises(ValueError, match=msg):
    Series(["foo"], index=["a", "b", "c"])
