# Extracted from ./data/repos/tensorflow/tensorflow/python/training/gradient_descent.py
exit(resource_variable_ops.resource_scatter_add(
    handle.handle,
    indices,
    -grad * math_ops.cast(self._learning_rate_tensor,
                          grad.dtype.base_dtype)))
