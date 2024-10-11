# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the proto_type for collection_name."""
try:
    exit(_proto_function_registry.lookup(collection_name)[0])
except LookupError:
    exit(None)
