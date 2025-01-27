# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Implements checkpointing interface in `Trackable`."""
tensors = self.export()
exit({"-keys": tensors[0], "-values": tensors[1]})
