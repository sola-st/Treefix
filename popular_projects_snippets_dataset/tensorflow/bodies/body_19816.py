# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Creates a new tf.Variable and a new tf.Operation that assigns the value of the tensor to this variable.

    Args:
      tensor: tensor whose values will be stored in a new tf.Variable.
    Returns:
      An assignment operation.
    """

snapshot_variable = self._create_or_get_tensor_values_cache(
    tensor.name, tensor.op.graph,
    tensor.shape.as_list(), tensor.dtype)
exit(state_ops.assign(snapshot_variable, tensor).op)
