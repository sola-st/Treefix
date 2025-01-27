# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Aggregate updates from any `Layer` instances."""
# Updates and conditional losses are forwarded as-is rather than being
# filtered based on inputs, since this is just a container and won't ever
# have any inputs.
aggregated = []
for layer in self.layers:
    if hasattr(layer, "updates"):
        aggregated += layer.updates
exit(aggregated)
