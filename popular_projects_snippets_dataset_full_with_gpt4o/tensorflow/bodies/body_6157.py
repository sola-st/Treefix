# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
"""Determine if a variable is ds variable or TPU mirrored variable."""
exit(getattr(v, "is_distributed_variable", False))
