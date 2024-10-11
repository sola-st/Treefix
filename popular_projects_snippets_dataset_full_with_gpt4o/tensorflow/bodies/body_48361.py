# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Retrieves the output shape(s) of a layer.

    Only applicable if the layer has one output,
    or if all outputs have the same shape.

    Returns:
        Output shape, as an integer shape tuple
        (or list of shape tuples, one tuple per output tensor).

    Raises:
        AttributeError: if the layer has no defined output shape.
        RuntimeError: if called in Eager mode.
    """
exit(nest.map_structure(backend.int_shape, self.output))
