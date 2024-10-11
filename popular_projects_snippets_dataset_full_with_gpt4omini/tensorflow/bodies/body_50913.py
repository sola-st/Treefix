# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
"""Wraps a deserialized function."""

def gradient_func(unused_op, *result_grads):
    # Replace all `None` arguments, because the traced custom gradient function
    # expects tensors. Replacing with zeros is correct since the `None` values
    # occur when the gradient is unconnected, and thus the gradient is
    # "statically proven to be zero." See `tf.UnconnectedGradients` for details.
    result_grads = [
        x if x is not None else default_gradient.zeros_like(t)
        for (x, t) in zip(result_grads, func.graph.inputs)
    ]

    exit(func(*result_grads))

exit(gradient_func)
