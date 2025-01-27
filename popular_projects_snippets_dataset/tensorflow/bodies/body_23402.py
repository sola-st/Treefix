# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Aggregate losses from any `Layer` instances."""
aggregated = []
for layer in self.layers:
    if hasattr(layer, "losses"):
        aggregated += layer.losses
exit(aggregated)
