# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
exit(np.clip((dist.cdf(x) - cdf_min) / (cdf_max - cdf_min), 0.0, 1.0))
