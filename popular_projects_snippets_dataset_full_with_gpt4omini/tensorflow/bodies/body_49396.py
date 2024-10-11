# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Creates a `SumOverBatchSizeMetricWrapper` instance.

    Args:
      fn: The metric function to wrap, with signature `fn(y_true, y_pred,
        **kwargs)`.
      name: (Optional) string name of the metric instance.
      dtype: (Optional) data type of the metric result.
      **kwargs: The keyword arguments that are passed on to `fn`.
    """
super(SumOverBatchSizeMetricWrapper, self).__init__(name=name, dtype=dtype)
self._fn = fn
self._fn_kwargs = kwargs
