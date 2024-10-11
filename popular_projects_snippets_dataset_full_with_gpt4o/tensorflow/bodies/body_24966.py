# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients.py
"""Register the gradient tensor for an x-tensor.

    Args:
      x_tensor_name: (`str`) the name of the independent `tf.Tensor`, i.e.,
        the tensor on the denominator of the differentiation.
      gradient_tensor: the gradient `tf.Tensor`.
    """
if len(_gradient_debuggers) == 1 or self._is_active_context:
    self._check_same_graph(gradient_tensor)
    self._gradient_tensors[x_tensor_name] = gradient_tensor
