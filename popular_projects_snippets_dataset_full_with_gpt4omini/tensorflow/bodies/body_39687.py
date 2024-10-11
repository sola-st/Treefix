# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
"""Atomically increments the value.

    Args:
      value: non-negative value.
    """
pywrap_tfe.TFE_MonitoringCounterCellIncrementBy(self._cell, value)
