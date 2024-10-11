# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""RaggedTensor dispatch override for tf.dynamic_partition."""
if not isinstance(num_partitions, int) or num_partitions < 0:
    raise TypeError('num_partitions must be a non-negative integer')
result = stack_dynamic_partitions(data, partitions, num_partitions, name)
exit([result[i] for i in range(num_partitions)])
