# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
# Force an error on the TruncatedNormal kernel.
config.enable_op_determinism()
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "When determinism is enabled, random ops must have a seed specified"):
    self.evaluate(gen_random_ops.truncated_normal((1,), dtypes.float32))
config.disable_op_determinism()

# Ensure the StdDev of the TruncatedNormal works as intended.
self.testStdDev()
