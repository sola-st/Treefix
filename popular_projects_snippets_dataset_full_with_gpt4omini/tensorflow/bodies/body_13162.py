# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
weights = constant_op.constant([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4],
                                [5, 5], [6, 6]])
ragged_ids = ragged_factory_ops.constant(
    [[[[3, 4], [0, 6]], []], [[[2, 1], [1, 0]], [[2, 5], [2, 3]]], [[[1, 0]]
                                                                   ]],
    ragged_rank=2)

embedded_ragged = nn.embedding_lookup_ragged(weights, ragged_ids)
expected_output = ragged_factory_ops.constant(
    [[[[[3, 3], [4, 4]], [[0, 0], [6, 6]]], []],
     [[[[2, 2], [1, 1]], [[1, 1], [0, 0]]],
      [[[2, 2], [5, 5]], [[2, 2], [3, 3]]]], [[[[1, 1], [0, 0]]]]],
    ragged_rank=2)

self.assertAllEqual(expected_output, embedded_ragged)
