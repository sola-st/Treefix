# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/array_ops_test.py
with self.assertRaisesRegex(
    errors.FailedPreconditionError,
    "Attempting to use uninitialized value Variable"):
    v = variables.VariableV1([1, 2])
    self.evaluate(v[:].assign([1, 2]))
