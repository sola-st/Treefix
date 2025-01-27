# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
"""Atomically set the value.

    Args:
      value: integer value.
    """
pywrap_tfe.TFE_MonitoringIntGaugeCellSet(self._cell, value)
