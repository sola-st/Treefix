# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
with self.assertRaisesRegex(
    RuntimeError,
    "Random ops require a seed to be set when determinism is enabled."):
    random_ops.random_normal((1,))
with self.assertRaisesRegex(
    RuntimeError,
    "Random ops require a seed to be set when determinism is enabled."):
    random_ops.truncated_normal((1,))
with self.assertRaisesRegex(
    RuntimeError,
    "Random ops require a seed to be set when determinism is enabled."):
    random_ops.random_uniform((1,))
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "When determinism is enabled, random ops must have a seed specified"):
    self.evaluate(gen_random_ops.random_standard_normal((1,), dtypes.float32))
