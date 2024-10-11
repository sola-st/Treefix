# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/candidate_sampler_ops_test.py
with self.cached_session():
    true_classes = constant_op.constant(
        [[1, 2], [0, 4], [3, 3]], dtype=dtypes.int64)
    _, true_expected_count, _ = candidate_sampling_ops.all_candidate_sampler(
        true_classes, self.NUM_TRUE, self.NUM_SAMPLED, True)
    true_log_expected_count = math_ops.log(true_expected_count)
    result = self.evaluate(true_log_expected_count)

self.assertAllEqual(result, [[0.0] * self.NUM_TRUE] * self.BATCH_SIZE)
self.assertEqual(true_expected_count.get_shape(),
                 [self.BATCH_SIZE, self.NUM_TRUE])
self.assertEqual(true_log_expected_count.get_shape(),
                 [self.BATCH_SIZE, self.NUM_TRUE])
