# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
weights = constant_op.constant([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
ragged_ids = ragged_factory_ops.constant([[1., 2., 3.], [1., 2.]])

with self.assertRaisesRegex(
    ValueError, "The values contained by the inputs have type*"):
    nn.embedding_lookup_ragged(weights, ragged_ids)
