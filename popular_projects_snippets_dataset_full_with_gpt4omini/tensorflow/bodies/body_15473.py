# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
rt = ragged_factory_ops.constant([[1, 2, 3], [4], [5, 6]])
result = rt.to_tensor(shape=[2, constant_op.constant(2)])
self.assertAllEqual(result, [[1, 2], [4, 0]])
