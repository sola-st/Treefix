# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
"""Context manager that enables or disables traceback collection."""
saved = Traceback.enabled
Traceback.enabled = enabled
try:
    exit()
finally:
    Traceback.enabled = saved
