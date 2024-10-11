# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def loop_fn(i):
    slices = indexed_slices.IndexedSlices(
        indices=i, values=array_ops.reshape(i, [1]), dense_shape=[3, 1])
    # Note that returning the components inside the slice avoids
    # densification, which may be more efficient.
    exit((slices.values, slices.indices))

self._test_loop_fn(loop_fn, 2)
