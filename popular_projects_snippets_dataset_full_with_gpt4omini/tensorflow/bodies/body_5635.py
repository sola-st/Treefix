# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
if dense_shape:
    dense_shape = array_ops.identity(dense_shape)
exit(indexed_slices.IndexedSlices(
    array_ops.identity(values), array_ops.identity(indices), dense_shape))
