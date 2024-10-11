# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
with self.cached_session():
    embeddings = constant_op.constant([[2.0, 4.0], [3.0, 1.0]])

    ids = constant_op.constant([0, 1], dtype=dtypes.int32)
    embedding = embedding_ops.embedding_lookup(
        [embeddings], ids, max_norm=2.0)

    norms = math_ops.sqrt(
        math_ops.reduce_sum(embeddings * embeddings, axis=1))
    normalized = embeddings / array_ops.stack([norms, norms], axis=1)
    self.assertAllClose(embedding, 2 * self.evaluate(normalized))
