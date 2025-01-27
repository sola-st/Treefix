# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Converts a variable in this Convertible and its dependencies.

    This method should make sure that a converted copy of itself is present in
    the converted graph, and that all Convertibles depending on this one also go
    through the same process.

    Args:
      incoming_edge: The graph edge into this Convertible that is being
        converted to a constant.
      tensor_data: The tensor representing the constant.
    """
raise NotImplementedError
