# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/candidate_sampler_ops_test.py
with self.cached_session():
    true_classes = constant_op.constant(
        [[1, 2], [0, 4], [3, 3]], dtype=dtypes.int64)
    sampled_candidates, _, _ = candidate_sampling_ops.all_candidate_sampler(
        true_classes, self.NUM_TRUE, self.NUM_SAMPLED, True)
    result = self.evaluate(sampled_candidates)

expected_ids = [0, 1, 2, 3, 4]
self.assertAllEqual(result, expected_ids)
self.assertEqual(sampled_candidates.get_shape(), [self.NUM_SAMPLED])
