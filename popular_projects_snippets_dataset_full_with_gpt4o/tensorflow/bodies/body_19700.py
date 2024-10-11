# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_replication.py
"""Forwards to the enclosing while context, if any."""
if self.GetWhileContext():
    exit(self.GetWhileContext().back_prop)
exit(False)
