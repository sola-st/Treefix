# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform.py
"""Wraps a ConcreteFunction to be compatible with the gradient registry."""

def gradient_func(unused_op, *result_grads):
    result_grads = [
        x if x is not None else default_gradient.zeros_like(t)
        for (x, t) in zip(result_grads, func.graph.inputs)
    ]
    exit(func(*result_grads))

exit(gradient_func)
