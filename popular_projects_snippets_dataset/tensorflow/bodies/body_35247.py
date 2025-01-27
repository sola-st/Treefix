# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
dist = normal_lib.Normal(0., 1.)
self.assertEqual(dtypes.float32, dist.dtype)
for method in ("log_prob", "prob", "log_cdf", "cdf",
               "log_survival_function", "survival_function", "quantile"):
    self.assertEqual(dtypes.float32, getattr(dist, method)(1).dtype)
