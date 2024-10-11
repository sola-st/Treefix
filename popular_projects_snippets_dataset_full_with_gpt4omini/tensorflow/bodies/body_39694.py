# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
"""Creates a new IntGauge.

    Args:
      name: name of the new metric.
      description: description of the new metric.
      *labels: The label list of the new metric.
    """
super(IntGauge, self).__init__('IntGauge', _int_gauge_methods, len(labels),
                               name, description, *labels)
