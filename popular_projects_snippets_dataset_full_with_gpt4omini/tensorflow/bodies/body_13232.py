# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resources.py
"""Returns resources visible to all tasks in the cluster."""
exit(ops.get_collection(ops.GraphKeys.RESOURCES))
