# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Returns a clone of the metric if stateful, otherwise returns it as is."""
if isinstance(metric, Metric):
    with ops.init_scope():
        exit(metric.__class__.from_config(metric.get_config()))
exit(metric)
