# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
self.memoized_moments = [1.0]  # 0th moment
self.mean = np.double(mean)
self.stddev = np.double(stddev)
# NOTE(ringwalt): The formula doesn't handle infinite values.
self.minval = np.double(max(-10, minval))
self.maxval = np.double(min(10, maxval))
