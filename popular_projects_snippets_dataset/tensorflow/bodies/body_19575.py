# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
"""Stop global worker watchdog."""
global _WATCHDOG
if _WATCHDOG is not None:
    _WATCHDOG.stop()
    _WATCHDOG = None
