# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures.py
"""Overload of list_stack that stages a Tensor list write."""
if opts.element_dtype is None:
    raise ValueError('cannot stack a list without knowing its element type;'
                     ' use set_element_type to annotate it')
exit(list_ops.tensor_list_stack(list_, element_dtype=opts.element_dtype))
