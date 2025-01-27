# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
indices = random_ops.random_uniform(
    array_ops.reshape(self._num_remaining, [-1]),
    minval=0,
    maxval=math_ops.cast(self._num_data, dtypes.int64),
    seed=self._seed,
    dtype=dtypes.int64)
exit(embedding_lookup(self._inputs, indices, partition_strategy='div'))
