# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients.py
"""Get the gradient tensor of an x-tensor.

    Args:
      x_tensor: (`tf.Tensor`, `tf.Variable` or `str`) The x-tensor object or its
        name. x-tensor refers to the independent `tf.Tensor`, i.e., the tensor
        on the denominator of the differentiation.

    Returns:
      If found, the gradient tensor.

    Raises:
      TypeError: If `x_tensor` is not a `tf.Tensor`, `tf.Variable` or `str`.
      LookupError: If the `x_tensor` has not been registered with a gradient
        tensor.
    """
x_tensor_name = self._get_tensor_name(x_tensor)
if x_tensor_name not in self._gradient_tensors:
    raise LookupError(
        "This GradientsDebugger has not received any gradient tensor for "
        "x-tensor %s" % x_tensor_name)
exit(self._gradient_tensors[x_tensor_name])
