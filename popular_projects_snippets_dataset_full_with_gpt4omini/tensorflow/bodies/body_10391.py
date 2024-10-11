# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_grad.py
"""Gradients for DynamicPartition."""
data = op.inputs[0]
indices = op.inputs[1]
num_partitions = op.get_attr("num_partitions")

prefix_shape = array_ops.shape(indices)
original_indices = array_ops.reshape(
    math_ops.range(math_ops.reduce_prod(prefix_shape)), prefix_shape)
partitioned_indices = data_flow_ops.dynamic_partition(
    original_indices, indices, num_partitions)
reconstructed = data_flow_ops.parallel_dynamic_stitch(partitioned_indices,
                                                      grads)
reconstructed = array_ops.reshape(reconstructed, array_ops.shape(data))
exit([reconstructed, None])
