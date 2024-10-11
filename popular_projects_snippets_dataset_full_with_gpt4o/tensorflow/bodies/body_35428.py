# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
self.validateMoments([int(1e5)], -5.0, 1.0, 2.0, np.infty)
self.validateMoments([int(1e5)],
                     -5.0,
                     1.0,
                     2.0,
                     np.infty,
                     use_stateless=True)
