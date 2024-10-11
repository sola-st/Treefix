# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# make sure we raise when comparing with different lengths, specific
#  to the case where one has length-1, which numpy would broadcast
arr = arr1d
idx = self.index_cls(arr)

with pytest.raises(ValueError, match="Lengths must match"):
    arr == arr[:1]

# test the index classes while we're at it, GH#23078
with pytest.raises(ValueError, match="Lengths must match"):
    idx <= idx[[0]]
