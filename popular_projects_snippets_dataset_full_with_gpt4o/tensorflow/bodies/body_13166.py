# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
weights = constant_op.constant(
    [[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]],
    dtype=dtypes.float32)
ragged_ids = ragged_factory_ops.constant([[1, 2, 3], [0], [1, 2]],
                                         ragged_rank=1)

actual_embeddings = [
    nn.embedding_lookup(weights, ragged_ids, max_norm=max_norm)
    for max_norm in [1, 2, 5]
]

expected_embeddings = (
    # max_norm = 1
    [[[.5, .5, .5, .5], [.5, .5, .5, .5], [.5, .5, .5, .5]], [[0, 0, 0, 0]],
     [[.5, .5, .5, .5], [.5, .5, .5, .5]]],
    # max_norm = 2
    [[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], [[0, 0, 0, 0]],
     [[1, 1, 1, 1], [1, 1, 1, 1]]],
    # max_norm = 5
    [[[1, 1, 1, 1], [2, 2, 2, 2], [2.5, 2.5, 2.5, 2.5]], [[0, 0, 0, 0]],
     [[1, 1, 1, 1], [2, 2, 2, 2]]],
)

for expected, actual in zip(expected_embeddings, actual_embeddings):
    self.assertAllClose(
        ragged_factory_ops.constant(expected, dtype=float, ragged_rank=1),
        actual)
