# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce_test.py
# 0 devices
pred_by_c_d, rank_by_c_d = ar._ring_permutations(1, 0, [])
self.assertEqual(pred_by_c_d, [])
self.assertEqual(rank_by_c_d, [])
# 1 worker, 1 subchunk cases
pred_by_c_d, rank_by_c_d = ar._ring_permutations(1, 1, [0])
self.assertEqual(pred_by_c_d, [[0]])
self.assertEqual(rank_by_c_d, [[0]])
pred_by_c_d, rank_by_c_d = ar._ring_permutations(1, 1, [0, 1, 2])
self.assertEqual(pred_by_c_d, [[2, 0, 1]])
self.assertEqual(rank_by_c_d, [[0, 1, 2]])
# multiple workers, 1 subchunk cases
pred_by_c_d, rank_by_c_d = ar._ring_permutations(2, 1, [0, 1, 2])
self.assertEqual(pred_by_c_d, [[5, 0, 1, 2, 3, 4]])
self.assertEqual(rank_by_c_d, [[0, 1, 2, 3, 4, 5]])
pred_by_c_d, rank_by_c_d = ar._ring_permutations(3, 1, [0, 1, 2])
self.assertEqual(pred_by_c_d, [[8, 0, 1, 2, 3, 4, 5, 6, 7]])
self.assertEqual(rank_by_c_d, [[0, 1, 2, 3, 4, 5, 6, 7, 8]])
pred_by_c_d, rank_by_c_d = ar._ring_permutations(2, 1, [2, 1, 0])
self.assertEqual(pred_by_c_d, [[1, 2, 3, 4, 5, 0]])
self.assertEqual(rank_by_c_d, [[2, 1, 0, 5, 4, 3]])
# 1 worker, multiple subchunk cases
pred_by_c_d, rank_by_c_d = ar._ring_permutations(1, 2, [0, 1, 2, 3])
self.assertEqual(pred_by_c_d, [[3, 0, 1, 2], [3, 0, 1, 2]])
self.assertEqual(rank_by_c_d, [[0, 1, 2, 3], [2, 3, 0, 1]])
pred_by_c_d, rank_by_c_d = ar._ring_permutations(1, 4, [0, 1, 2, 3])
self.assertEqual(pred_by_c_d, [[3, 0, 1, 2], [3, 0, 1, 2],
                               [3, 0, 1, 2], [3, 0, 1, 2]])
self.assertEqual(rank_by_c_d, [[0, 1, 2, 3], [3, 0, 1, 2],
                               [2, 3, 0, 1], [1, 2, 3, 0]])
# multiple worker, multiple subchunk cases
pred_by_c_d, rank_by_c_d = ar._ring_permutations(2, 2, [0, 1, 2, 3])
self.assertEqual(pred_by_c_d, [[7, 0, 1, 2, 3, 4, 5, 6],
                               [3, 0, 5, 2, 7, 4, 1, 6]])
self.assertEqual(rank_by_c_d, [[0, 1, 2, 3, 4, 5, 6, 7],
                               [2, 3, 0, 1, 6, 7, 4, 5]])
pred_by_c_d, rank_by_c_d = ar._ring_permutations(2, 2, [0, 3, 2, 1])
self.assertEqual(pred_by_c_d, [[5, 2, 3, 0, 1, 6, 7, 4],
                               [1, 2, 7, 0, 5, 6, 3, 4]])
self.assertEqual(rank_by_c_d, [[0, 3, 2, 1, 4, 7, 6, 5],
                               [2, 1, 0, 3, 6, 5, 4, 7]])
