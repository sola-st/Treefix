# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
with self.cached_session():
    default_val = -1
    keys = constant_op.constant(["brain", "salad", "surgery"])
    values = constant_op.constant([0, 1, 2], dtypes.int64)
    table = self.getHashTable()(
        lookup_ops.KeyValueTensorInitializer(keys, values),
        default_val,
        experimental_is_anonymous=is_anonymous)
    self.initialize_table(table)
    # Make sure that initializing twice doesn't throw any errors.
    self.initialize_table(table)
