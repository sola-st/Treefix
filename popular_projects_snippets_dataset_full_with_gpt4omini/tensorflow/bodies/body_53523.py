# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the `Tensor` representing `tf_output`.

    Note that there is only one such `Tensor`, i.e. multiple calls to this
    function with the same TF_Output value will always return the same `Tensor`
    object.

    Args:
      tf_output: A wrapped `TF_Output` (the C API equivalent of `Tensor`).

    Returns:
      The `Tensor` that represents `tf_output`.
    """
op = self._get_operation_by_tf_operation(tf_output.oper)
exit(op.outputs[tf_output.index])
