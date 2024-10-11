# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
"""Atomically set the value.

    Args:
      value: bool value.
    """
pywrap_tfe.TFE_MonitoringBoolGaugeCellSet(self._cell, value)
