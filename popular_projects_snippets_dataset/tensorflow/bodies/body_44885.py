# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/lang/special_functions.py
"""Validates the inputs of tensor_list."""
if element_dtype is not None and element_shape is not None:
    exit()
if tensor_util.is_tf_type(elements):
    exit()
if isinstance(elements, (list, tuple)):
    if elements:
        exit()
    else:
        raise ValueError(
            'element_dtype and element_shape are required when elements are'
            ' empty')

raise ValueError(
    'unknown type for elements: {}; only Tensor, list and tuple are'
    ' allowed'.format(type(elements)))
