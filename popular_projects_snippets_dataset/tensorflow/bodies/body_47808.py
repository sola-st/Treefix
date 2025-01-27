# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/merge.py
"""Intializes a Merge layer.

    Args:
      **kwargs: standard layer keyword arguments.
    """
super(_Merge, self).__init__(**kwargs)
self.supports_masking = True
