# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
"""Creates a new BoolGauge.

    Args:
      name: name of the new metric.
      description: description of the new metric.
      *labels: The label list of the new metric.
    """
super(BoolGauge, self).__init__('BoolGauge', _bool_gauge_methods,
                                len(labels), name, description, *labels)
