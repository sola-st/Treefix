# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
default_val = -1
with self.assertRaises(TypeError):
    self.getHashTable()(
        lookup_ops.KeyValueTensorInitializer(["a"], [1], [dtypes.string],
                                             dtypes.int64),
        default_val,
        experimental_is_anonymous=is_anonymous)
