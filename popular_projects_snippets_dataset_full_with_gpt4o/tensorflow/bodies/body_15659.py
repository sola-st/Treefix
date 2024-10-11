# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_check_ops.py
exit(check_ops.assert_type(tensor.flat_values, tf_type,
                             message=message, name=name))
