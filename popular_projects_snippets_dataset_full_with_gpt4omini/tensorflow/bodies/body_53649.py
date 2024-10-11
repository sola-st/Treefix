# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the to_proto function for collection_name."""
try:
    exit(_proto_function_registry.lookup(collection_name)[1])
except LookupError:
    exit(None)
