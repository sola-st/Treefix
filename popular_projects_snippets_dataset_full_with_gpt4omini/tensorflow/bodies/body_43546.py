# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Returns a list of TensorFlow APIs that support type-based dispatch."""
exit(sorted(
    _TYPE_BASED_DISPATCH_SIGNATURES,
    key=lambda api: f"{api.__module__}.{api.__name__}"))
