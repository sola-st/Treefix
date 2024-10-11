# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sobol_ops_test.py
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            r'Shape must be rank 0 but is rank 1|'
                            r'\w+ must be a scalar'):
    self.evaluate(gen_math_ops.sobol_sample(
        dim=7,
        num_results=constant_op.constant([1, 0]),
        skip=constant_op.constant([1])))
