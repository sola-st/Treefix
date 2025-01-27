# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
exit(check_ops.assert_non_negative(
    tensor[1:] - tensor[:-1], message=message))
