# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
with self.cached_session():
    embeddings = constant_op.constant([[2.0]])

    ids = constant_op.constant([0], dtype=dtypes.int32)
    embedding = embedding_ops.embedding_lookup(
        [embeddings], ids, max_norm=1.0)

    self.assertAllEqual(embedding, [[1.0]])
