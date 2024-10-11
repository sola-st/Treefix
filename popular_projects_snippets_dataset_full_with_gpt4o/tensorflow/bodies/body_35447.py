# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/candidate_sampler_ops_test.py
with self.cached_session():
    true_classes = constant_op.constant(
        [[1, 2], [0, 4], [3, 3]], dtype=dtypes.int64)
    _, _, sampled_expected_count = candidate_sampling_ops.all_candidate_sampler(  # pylint: disable=line-too-long
        true_classes, self.NUM_TRUE, self.NUM_SAMPLED, True)
    sampled_log_expected_count = math_ops.log(sampled_expected_count)
    result = self.evaluate(sampled_log_expected_count)

self.assertAllEqual(result, [0.0] * self.NUM_SAMPLED)
self.assertEqual(sampled_expected_count.get_shape(), [self.NUM_SAMPLED])
self.assertEqual(sampled_log_expected_count.get_shape(), [self.NUM_SAMPLED])
