# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
self.const_a = constant_op.constant(11.0, name="a")
self.const_b = constant_op.constant(22.0, name="b")
self.const_c = constant_op.constant(33.0, name="c")

self.sparse_d = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 1]], values=[1.0, 2.0], dense_shape=[3, 3])
