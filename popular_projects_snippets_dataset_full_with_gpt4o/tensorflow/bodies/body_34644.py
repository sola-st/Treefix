# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
with self.cached_session():
    default_val = -1
    table = self.getHashTable()(
        lookup_ops.KeyValueTensorInitializer(["a"], [1],
                                             value_dtype=dtypes.int64),
        default_val,
        experimental_is_anonymous=is_anonymous)

    input_string = constant_op.constant(["brain", "salad", "surgery"])
    output = table.lookup(input_string)

    with self.assertRaisesOpError("Table not initialized"):
        self.evaluate(output)
