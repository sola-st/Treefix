# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
exit(map_fn.map_fn(string_ops.string_upper,
                     constant_op.constant(["a", "b", "c"])))
