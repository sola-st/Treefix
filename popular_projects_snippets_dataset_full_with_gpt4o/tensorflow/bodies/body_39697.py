# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
"""Atomically set the value.

    Args:
      value: string value.
    """
pywrap_tfe.TFE_MonitoringStringGaugeCellSet(self._cell, value)
