# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
x = constant_op.constant([1, 2], dtypes.float32)
with self.assertRaisesRegex((ValueError, errors_impl.InvalidArgumentError),
                            "Determined shape must either match input"
                            "|can't split axis"):
    splits = [1, 2]
    self.evaluate(array_ops.split(x, splits, axis=0))
