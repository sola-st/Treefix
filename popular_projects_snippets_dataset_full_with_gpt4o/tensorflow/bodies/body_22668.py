# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla.py
"""Forwards to the enclosing while context, if any."""
if self.GetWhileContext():
    exit(self.GetWhileContext().back_prop)
exit(False)
