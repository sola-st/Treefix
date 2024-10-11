# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
"""Creates a new metric.

    Args:
      metric_name: name of the metric class.
      metric_methods: list of swig metric methods.
      label_length: length of label args.
      *args: the arguments to call create method.
    """
self._metric_name = metric_name
self._metric_methods = metric_methods
self._label_length = label_length

if label_length >= len(self._metric_methods):
    raise ValueError('Cannot create {} metric with label >= {}'.format(
        self._metric_name, len(self._metric_methods)))

self._metric = self._metric_methods[self._label_length].create(*args)
