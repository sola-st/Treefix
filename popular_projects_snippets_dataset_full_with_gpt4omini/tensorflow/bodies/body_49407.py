# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Clones the given metric list/dict."""
exit(nest.map_structure(clone_metric, metrics))
