# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/numpy_util.py
"""Creates uniform random tensor with the given layout."""
exit(api.relayout(
    stateless_random_ops.stateless_random_uniform(shape=shape, seed=seed),
    layout=layout,
))
