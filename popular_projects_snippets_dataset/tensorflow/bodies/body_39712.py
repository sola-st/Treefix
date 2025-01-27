# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
"""Creates a new Sampler.

    Args:
      name: name of the new metric.
      buckets: bucketing strategy of the new metric.
      description: description of the new metric.
      *labels: The label list of the new metric.
    """
super(Sampler, self).__init__('Sampler', _sampler_methods, len(labels),
                              name, buckets.buckets, description, *labels)
