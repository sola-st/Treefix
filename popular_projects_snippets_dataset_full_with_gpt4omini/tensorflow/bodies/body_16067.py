# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_fn_op_test.py
tokens_val, indices_val = x
exit(array_ops.gather(tokens_val, indices_val))
