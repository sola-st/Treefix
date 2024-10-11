# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
self.validateKolmogorovSmirnov([int(1e5)], 10.0, 1.0, 4.0, np.infty)
self.validateKolmogorovSmirnov([int(1e5)],
                               10.0,
                               1.0,
                               4.0,
                               np.infty,
                               use_stateless=True)
