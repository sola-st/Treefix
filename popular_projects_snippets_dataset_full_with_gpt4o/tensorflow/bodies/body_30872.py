# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
assert vocab_size > 0
assert embed_dim > 0
assert num_shards > 0
assert num_shards <= vocab_size

initializer = init_ops.truncated_normal_initializer(
    mean=0.0, stddev=1.0 / math.sqrt(vocab_size), dtype=dtypes.float32)
embedding_weights = list(variable_scope.get_variable(
    name="embedding_weights",
    shape=[vocab_size, embed_dim],
    partitioner=partitioned_variables.fixed_size_partitioner(num_shards),
    initializer=initializer))
for w in embedding_weights:
    self.evaluate(w.initializer)
embedding_weights = [self.evaluate(w) for w in embedding_weights]
exit(embedding_weights)
