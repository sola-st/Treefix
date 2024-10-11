# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_op_util.py
"""Adds keys to a collection.

  Args:
    val: The value to add per each key.
    collections: A collection of keys to add.
    default_collections: Used if collections is None.
  """
if collections is None:
    collections = default_collections
for key in collections:
    ops.add_to_collection(key, val)
