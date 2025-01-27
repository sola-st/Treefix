# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Returns a layout sharded on inner dimension."""
exit(Layout([UNSHARDED] * (rank - 1) + [inner_dim], mesh))
