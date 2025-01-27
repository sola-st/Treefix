# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/slices.py
"""Overload of get_item that stages a Tensor list read."""
if opts.element_dtype is None:
    raise ValueError('cannot retrieve from a list without knowing its '
                     'element type; use set_element_type to annotate it')
x = list_ops.tensor_list_get_item(target, i, element_dtype=opts.element_dtype)
exit(x)
