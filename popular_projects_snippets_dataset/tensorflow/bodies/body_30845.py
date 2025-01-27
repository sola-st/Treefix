# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
p, params, feed_dict = _EmbeddingParams(
    num_shards, vocab_size, dtype=dtype, shape=shape)
shape = shape or [10]
partitioned_variable = variable_scope.get_variable(
    "p",
    shape=[vocab_size] + shape,
    initializer=array_ops.concat([params[p_i.name] for p_i in p], 0),
    partitioner=partitioned_variables.min_max_variable_partitioner(
        max_partitions=num_shards, min_slice_size=1),
    use_resource=use_resource)
exit((p, partitioned_variable, params, feed_dict))
