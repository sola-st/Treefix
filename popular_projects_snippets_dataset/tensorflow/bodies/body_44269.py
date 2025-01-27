# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/data_structures.py
"""Overload of new_list that stages a Tensor list creation."""
elements = tuple(ops.convert_to_tensor(el) for el in elements)

all_dtypes = set(el.dtype for el in elements)
if len(all_dtypes) == 1:
    inferred_dtype, = tuple(all_dtypes)
    if element_dtype is not None and element_dtype != inferred_dtype:
        raise ValueError(
            'incompatible dtype; specified: {}, inferred from {}: {}'.format(
                element_dtype, elements, inferred_dtype))
elif len(all_dtypes) > 1:
    raise ValueError(
        'TensorArray requires all elements to have the same dtype:'
        ' {}'.format(elements))
else:
    if element_dtype is None:
        raise ValueError('dtype is required to create an empty TensorArray')

all_shapes = set(tuple(el.shape.as_list()) for el in elements)
if len(all_shapes) == 1:
    inferred_shape, = tuple(all_shapes)
    if element_shape is not None and element_shape != inferred_shape:
        raise ValueError(
            'incompatible shape; specified: {}, inferred from {}: {}'.format(
                element_shape, elements, inferred_shape))
elif len(all_shapes) > 1:
    raise ValueError(
        'TensorArray requires all elements to have the same shape:'
        ' {}'.format(elements))
    # TODO(mdan): We may want to allow different shapes with infer_shape=False.
else:
    inferred_shape = None

if element_dtype is None:
    element_dtype = inferred_dtype
if element_shape is None:
    element_shape = inferred_shape

l = tensor_array_ops.TensorArray(
    dtype=element_dtype,
    size=len(elements),
    dynamic_size=True,
    infer_shape=(element_shape is None),
    element_shape=element_shape)
for i, el in enumerate(elements):
    l = l.write(i, el)
exit(l)
