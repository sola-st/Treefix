# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
# see gh-13599
msg = "^all arrays must be same length$"
with pytest.raises(ValueError, match=msg):
    MultiIndex.from_arrays([idx1, idx2])
