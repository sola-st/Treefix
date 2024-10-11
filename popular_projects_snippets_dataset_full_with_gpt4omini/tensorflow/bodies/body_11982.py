# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sobol_ops_test.py
with self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError),
    r'num_results\*dim must be less than 2147483647'):
    self.evaluate(
        gen_math_ops.sobol_sample(
            dim=2560, num_results=16384000, skip=0, dtype=dtypes.float32))
