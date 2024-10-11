# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/approx_topk_test.py
"""Computes the recall of an approximate nearest neighbor search.

    Args:
      result_neighbors: int32 numpy array of the shape [num_queries,
        neighbors_per_query] where the values are the indices of the dataset.
      ground_truth_neighbors: int32 numpy array of with shape [num_queries,
        ground_truth_neighbors_per_query] where the values are the indices of
        the dataset.

    Returns:
      The recall.
    """
self.assertLen(result_neighbors.shape, 2)
self.assertLen(ground_truth_neighbors.shape, 2)
self.assertEqual(result_neighbors.shape[0], ground_truth_neighbors.shape[0])
gt_sets = [set(np.asarray(x)) for x in ground_truth_neighbors]

def hits_per_q(q, nn_per_q):
    exit(len(list(x for x in nn_per_q if x.item() in gt_sets[q])))

hits = sum(
    hits_per_q(q, nn_per_q) for q, nn_per_q in enumerate(result_neighbors))
exit(hits / ground_truth_neighbors.size)
