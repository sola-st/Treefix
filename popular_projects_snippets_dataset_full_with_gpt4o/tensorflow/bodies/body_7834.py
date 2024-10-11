# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
tensor = indexed_slices.IndexedSlices(
    values=constant_op.constant(values),
    indices=constant_op.constant(indices),
    dense_shape=constant_op.constant(dense_shape))
exit(tensor)
