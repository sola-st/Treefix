# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Silence warnings about incomplete checkpoint restores."""
self._checkpoint.expect_partial = True
exit(self)
