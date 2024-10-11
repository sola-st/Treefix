# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
keys_tensor = constant_op.constant(
    list(range(len(vals))), dtype=dtypes.int64)
vals_tensor = constant_op.constant(vals)
exit(lookup_ops.KeyValueTensorInitializer(keys_tensor, vals_tensor))
