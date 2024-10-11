# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/candidate_sampler_ops_test.py
with self.cached_session() as sess:
    indices = constant_op.constant([0, 0, 1, 1, 2, 2])
    true_candidates_vec = constant_op.constant([1, 2, 0, 4, 3, 3])
    true_candidates_matrix = array_ops.reshape(
        true_candidates_vec, [self.BATCH_SIZE, self.NUM_TRUE])
    indices_val, true_candidates_val = sess.run(
        [indices, true_candidates_matrix])

self.assertAllEqual(indices_val, [0, 0, 1, 1, 2, 2])
self.assertAllEqual(true_candidates_val, self.TRUE_LABELS)
