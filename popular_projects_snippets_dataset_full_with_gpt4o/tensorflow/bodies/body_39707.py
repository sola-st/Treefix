# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
"""Atomically add a sample.

    Args:
      value: float value.
    """
pywrap_tfe.TFE_MonitoringSamplerCellAdd(self._cell, value)
