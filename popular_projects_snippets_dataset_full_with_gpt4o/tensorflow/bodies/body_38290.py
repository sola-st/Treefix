# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
# Test case for GitHub issue 40653.
for use_gpu in [True, False]:
    with self.cached_session(use_gpu=use_gpu):
        with self.assertRaisesRegex(
            (ValueError, errors_impl.InvalidArgumentError),
            "must be at least rank 1"):
            s = math_ops.segment_mean(
                data=np.uint16(10), segment_ids=np.array([]).astype("int64"))
            self.evaluate(s)
