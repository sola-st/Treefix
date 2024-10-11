# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Returns the destinations for batch all-reduce."""
if isinstance(x, ops.Tensor):
    # If this is a one device strategy.
    exit(x.device)
else:
    exit(x)
