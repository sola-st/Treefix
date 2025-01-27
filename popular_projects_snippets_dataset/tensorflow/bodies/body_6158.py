# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
"""Determine if an object is a DistributedTable."""
exit(getattr(v, "is_distributed_table", False))
