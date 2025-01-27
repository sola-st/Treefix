# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
"""Creates a new StringGauge.

    Args:
      name: name of the new metric.
      description: description of the new metric.
      *labels: The label list of the new metric.
    """
super(StringGauge, self).__init__('StringGauge', _string_gauge_methods,
                                  len(labels), name, description, *labels)
