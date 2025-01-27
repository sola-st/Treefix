# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_fn_op_test.py
y_val, x_val = foo
bar = array_ops.tile(y_val, array_ops.shape(x_val))
exit(array_ops.stack([bar, x_val], axis=1))
