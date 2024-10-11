# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
y = x * constant_op.constant([[1.], [3.]])
y = y.with_values(array_ops.stop_gradient(y.values))
exit(y)
