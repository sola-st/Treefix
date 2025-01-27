# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
x = constant_op.constant([1, 2, 3], dtypes.float32)
# A size of -1 signifies to determine size based on sum of other splits.
with self.assertRaisesRegex((ValueError, errors_impl.InvalidArgumentError),
                            "Split size at index 1 must be >= .*. Got: -2"):
    splits = [-1, -2]
    self.evaluate(array_ops.split(x, splits, axis=0))
