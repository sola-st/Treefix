# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
msg = "Input must be a list / sequence of array-likes"
with pytest.raises(TypeError, match=msg):
    MultiIndex.from_arrays(arrays=invalid_sequence_of_arrays)
