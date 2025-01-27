# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
# TODO(apassos) figure out how to unify these errors
with self.assertRaises(errors.InvalidArgumentError if context
                       .executing_eagerly() else ValueError):
    array_ops.scatter_nd(
        indices=[0],  # this should be indices=[[0]]
        updates=[0.0],
        shape=[1])
