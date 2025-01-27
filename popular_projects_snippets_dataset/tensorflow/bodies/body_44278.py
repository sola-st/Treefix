# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures.py
"""Overload of list_pop that stages a Tensor list pop."""
if i is not None:
    raise NotImplementedError('tensor lists only support removing from the end')

if opts.element_dtype is None:
    raise ValueError('cannot pop from a list without knowing its element '
                     'type; use set_element_type to annotate it')
if opts.element_shape is None:
    raise ValueError('cannot pop from a list without knowing its element '
                     'shape; use set_element_type to annotate it')
list_out, x = list_ops.tensor_list_pop_back(
    list_, element_dtype=opts.element_dtype)
x.set_shape(opts.element_shape)
exit((list_out, x))
