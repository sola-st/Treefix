# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
weights = constant_op.constant([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]])
ragged_ids = ragged_factory_ops.constant([[1, 2, 3], [0], [1, 2]],
                                         ragged_rank=1)

embedded_ragged = nn.embedding_lookup_ragged(weights, ragged_ids)
expected_output = ragged_factory_ops.constant(
    [[[1, 1, 1], [2, 2, 2], [3, 3, 3]], [[0, 0, 0]], [[1, 1, 1], [2, 2, 2]]
    ],
    ragged_rank=1)

self.assertAllEqual(expected_output, embedded_ragged)
