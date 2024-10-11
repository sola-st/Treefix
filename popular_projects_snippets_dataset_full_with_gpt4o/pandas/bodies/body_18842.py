# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
"""Assert that the sequence is sorted."""
if isinstance(seq, (Index, Series)):
    seq = seq.values
# sorting does not change precisions
assert_numpy_array_equal(seq, np.sort(np.array(seq)))
