# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Asserts that the output shape from the layer matches the actual shape."""
if len(expected) != len(actual):
    raise AssertionError(
        'When testing layer %s, for input %s, found output_shape='
        '%s but expected to find %s.\nFull kwargs: %s' %
        (layer_cls.__name__, x, actual, expected, kwargs))

for expected_dim, actual_dim in zip(expected, actual):
    if isinstance(expected_dim, tensor_shape.Dimension):
        expected_dim = expected_dim.value
    if isinstance(actual_dim, tensor_shape.Dimension):
        actual_dim = actual_dim.value
    if expected_dim is not None and expected_dim != actual_dim:
        raise AssertionError(
            'When testing layer %s, for input %s, found output_shape='
            '%s but expected to find %s.\nFull kwargs: %s' %
            (layer_cls.__name__, x, actual, expected, kwargs))
