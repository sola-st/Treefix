# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad_test.py
exit(array_ops.gather_v2(
    x, constant_op.constant([[2, 0], [2, 4]], dtype=dtypes.int32)))
