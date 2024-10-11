# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
# The randn sampler is used as the bounds are moved farther from the mean,
# and the probability of accepting a sample increases the farther the
# bounds are from the mean.
# This test asserts that at the point of switchover, both samplers are
# working (not raising an error or returning nan) and returning the
# expected moments.
use_gpu = test.is_gpu_available()
stddev_inside_bounds_before_using_randn = (
    _get_stddev_inside_bounds_before_using_randn(use_gpu))

epsilon = 0.001
self.validateMoments(
    shape=[int(1e6)],
    mean=0.,
    stddev=1.0,
    minval=-epsilon,
    maxval=stddev_inside_bounds_before_using_randn - epsilon)
self.validateMoments(
    shape=[int(1e6)],
    mean=0.,
    stddev=1.0,
    minval=-epsilon,
    maxval=stddev_inside_bounds_before_using_randn + epsilon)

self.validateMoments(
    shape=[int(1e6)],
    mean=0.,
    stddev=1.0,
    minval=-epsilon,
    maxval=stddev_inside_bounds_before_using_randn - epsilon,
    use_stateless=True)
self.validateMoments(
    shape=[int(1e6)],
    mean=0.,
    stddev=1.0,
    minval=-epsilon,
    maxval=stddev_inside_bounds_before_using_randn + epsilon,
    use_stateless=True)
