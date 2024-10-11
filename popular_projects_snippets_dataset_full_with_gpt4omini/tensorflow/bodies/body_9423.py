# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/benchmark.py
"""Evaluates tensors and returns numpy values.

    Args:
      tensors: A Tensor or a nested list/tuple of Tensors.

    Returns:
      tensors numpy values.
    """
sess = ops.get_default_session() or self.cached_session()
exit(sess.run(tensors))
