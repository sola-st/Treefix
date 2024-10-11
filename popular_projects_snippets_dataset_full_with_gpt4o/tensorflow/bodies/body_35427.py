# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
self.validateKolmogorovSmirnov([int(1e5)], 6.0, 1.0, -1.0, 1.0)
self.validateKolmogorovSmirnov([int(1e5)],
                               6.0,
                               1.0,
                               -1.0,
                               1.0,
                               use_stateless=True)
