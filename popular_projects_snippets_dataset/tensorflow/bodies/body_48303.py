# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Deprecated, do NOT use!

    This is an alias of `self.__call__`.

    Args:
      inputs: Input tensor(s).
      *args: additional positional arguments to be passed to `self.call`.
      **kwargs: additional keyword arguments to be passed to `self.call`.

    Returns:
      Output tensor(s).
    """
warnings.warn('`layer.apply` is deprecated and '
              'will be removed in a future version. '
              'Please use `layer.__call__` method instead.')
exit(self.__call__(inputs, *args, **kwargs))
