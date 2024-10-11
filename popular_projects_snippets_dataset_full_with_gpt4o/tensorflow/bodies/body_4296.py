# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Returns a layout sharded on batch dimension."""
exit(Layout([batch_dim] + [UNSHARDED] * (rank - 1), mesh))
