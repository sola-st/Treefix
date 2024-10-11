# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/candidate_sampler_ops_test.py
with self.cached_session() as sess:
    true_classes = constant_op.constant(
        [[1, 2], [0, 4], [3, 3]], dtype=dtypes.int64)
    sampled_candidates, _, _ = candidate_sampling_ops.all_candidate_sampler(
        true_classes, self.NUM_TRUE, self.NUM_SAMPLED, True)
    accidental_hits = candidate_sampling_ops.compute_accidental_hits(
        true_classes, sampled_candidates, self.NUM_TRUE)
    indices, ids, weights = self.evaluate(accidental_hits)

self.assertEqual(1, accidental_hits[0].get_shape().ndims)
self.assertEqual(1, accidental_hits[1].get_shape().ndims)
self.assertEqual(1, accidental_hits[2].get_shape().ndims)
for index, id_, weight in zip(indices, ids, weights):
    self.assertTrue(id_ in self.TRUE_LABELS[index])
    self.assertLess(weight, -1.0e37)
