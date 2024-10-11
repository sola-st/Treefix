# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_ops_test.py
del dtype, partition_info  # Unused by this unit-testing initializer.
exit(array_ops.tile(
    constant_op.constant([[self.init_val]], dtype=dtypes.float32), shape))
