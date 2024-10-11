# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad_test.py
exit(array_ops.gather_v2(
    x,
    constant_op.constant([[1, 0], [0, 0]], dtype=dtypes.int32),
    axis=1,
    batch_dims=1))
