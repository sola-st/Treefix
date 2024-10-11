# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resources.py
"""Returns resources intended to be local to this session."""
exit(ops.get_collection(ops.GraphKeys.LOCAL_RESOURCES))
