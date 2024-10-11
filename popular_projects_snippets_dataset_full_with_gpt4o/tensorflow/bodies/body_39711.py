# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
"""Creates a new exponential Buckets.

    Args:
      scale: float
      growth_factor: float
      bucket_count: integer
    """
super(ExponentialBuckets, self).__init__(
    pywrap_tfe.TFE_MonitoringNewExponentialBuckets(scale, growth_factor,
                                                   bucket_count))
