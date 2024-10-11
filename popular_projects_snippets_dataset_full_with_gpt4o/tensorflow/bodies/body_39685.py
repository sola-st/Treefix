# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
"""Retrieves the cell."""
if len(labels) != self._label_length:
    raise ValueError('The {} expects taking {} labels'.format(
        self._metric_name, self._label_length))
exit(self._metric_methods[self._label_length].get_cell(
    self._metric, *labels))
