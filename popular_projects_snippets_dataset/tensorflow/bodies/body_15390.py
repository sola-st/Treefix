# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
exit(check_ops.assert_equal(
    tensor, constant_op.constant(0, dtype=tensor.dtype), message=message))
