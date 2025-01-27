# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/kullback_leibler.py
"""Initialize the KL registrar.

    Args:
      dist_cls_a: the class of the first argument of the KL divergence.
      dist_cls_b: the class of the second argument of the KL divergence.
    """
self._key = (dist_cls_a, dist_cls_b)
