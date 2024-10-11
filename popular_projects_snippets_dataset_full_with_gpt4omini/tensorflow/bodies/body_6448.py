# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
value = indexed_slices.IndexedSlices(
    values=array_ops.identity([3]),
    indices=array_ops.identity([1]),
    dense_shape=(3,))
exit(v.scatter_update(value))
