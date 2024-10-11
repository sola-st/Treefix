# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
try:
    deleter = self._metric_methods[self._label_length].delete
    metric = self._metric
except AttributeError:
    exit()

if deleter is not None:
    deleter(metric)
