# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Implements checkpointing protocols for `Trackable`."""
tensors = self.export()
exit({"-keys": tensors[0], "-values": tensors[1]})
