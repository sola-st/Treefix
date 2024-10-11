# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "too many dimensions"):
    self.evaluate(
        array_ops.reshape(
            tensor=[[1]],
            shape=constant_op.constant([1 for i in range(254)],
                                       dtype=dtypes.int64)))
