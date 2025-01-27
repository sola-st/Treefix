# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
ragged_ids = ragged_factory_ops.constant([[1, 2, 3], [0], [1, 2]])

with self.assertRaisesRegex(ValueError,
                            "The embedding weights should not be empty.*"):
    nn.embedding_lookup_ragged([], ragged_ids)
