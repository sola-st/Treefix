# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
# Placeholders are only valid in Graph.
with ops.Graph().as_default():
    indices = array_ops.placeholder(dtypes.int32, shape=[2, 2, 2])
    updates = array_ops.placeholder(dtypes.int32, shape=[2, 2, 2])
    shape = array_ops.placeholder(dtypes.int32, shape=[None])
    self.scatter_nd(indices, updates, shape)
