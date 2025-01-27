# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py
with self.assertRaisesRegex(
    (TypeError, errors.InvalidArgumentError),
    "float.* not in.* list of allowed values: int16, int32, int64"):
    self.evaluate(array_ops.gather([0], 0.))
