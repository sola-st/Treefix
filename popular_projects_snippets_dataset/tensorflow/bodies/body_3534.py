# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform.py
result_grads = [
    x if x is not None else default_gradient.zeros_like(t)
    for (x, t) in zip(result_grads, func.graph.inputs)
]
exit(func(*result_grads))
