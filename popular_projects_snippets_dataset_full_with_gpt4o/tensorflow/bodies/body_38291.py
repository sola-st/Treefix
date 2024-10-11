# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
# Test case for GitHub issue 46888.
for op in [
    math_ops.segment_max,
    math_ops.segment_min,
    math_ops.segment_mean,
    math_ops.segment_sum,
    math_ops.segment_prod,
]:
    with self.cached_session(use_gpu=False):
        with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
            s = op(data=np.ones((1, 10, 1)), segment_ids=[1676240524292489355])
            self.evaluate(s)
