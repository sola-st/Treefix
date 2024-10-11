# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/logging_ops.py
if collections is None:
    collections = default_collections
for key in collections:
    ops.add_to_collection(key, val)
