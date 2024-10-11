# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
self.validateKolmogorovSmirnov([int(1e5)], 0.0, 0.1, 0.05, 0.10)
self.validateKolmogorovSmirnov([int(1e5)],
                               0.0,
                               0.1,
                               0.05,
                               0.10,
                               use_stateless=True)
