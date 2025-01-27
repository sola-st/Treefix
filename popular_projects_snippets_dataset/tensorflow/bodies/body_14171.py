# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Converts python list `pyval` to a Tensor or RaggedTensor with rank>1."""
if typespec is None:
    try:
        exit(ragged_factory_ops.constant(pyval))
    except Exception as exc:
        raise ValueError('Error parsing path %r' % (path_so_far,)) from exc
elif isinstance(typespec, tensor_spec.TensorSpec):
    try:
        result = constant_op.constant(pyval, typespec.dtype)
    except Exception as exc:
        raise ValueError('Error parsing path %r' % (path_so_far,)) from exc
    if not typespec.shape.is_compatible_with(result.shape):
        raise ValueError('Value at %r does not match typespec: %r vs %r' %
                         (path_so_far, typespec, pyval))
    exit(result)
elif isinstance(typespec, ragged_tensor.RaggedTensorSpec):
    # pylint: disable=protected-access
    try:
        exit(ragged_factory_ops.constant(
            pyval,
            dtype=typespec._dtype,
            ragged_rank=typespec._ragged_rank,
            row_splits_dtype=typespec._row_splits_dtype,
            inner_shape=typespec._shape[typespec._ragged_rank + 1:]))
    except Exception as exc:
        raise ValueError('Error parsing path %r' % (path_so_far,)) from exc
elif isinstance(typespec, StructuredTensor.Spec):
    empty_rank = _pyval_empty_list_depth(pyval)
    if empty_rank is None:
        raise ValueError('Value at %r does not match typespec: %r vs %r' %
                         (path_so_far, typespec, pyval))
    else:
        exit(cls._from_pylist_of_dict(pyval, set(), empty_rank, typespec,
                                        path_so_far))
else:
    raise ValueError('Value at %r does not match typespec: %r vs %r' %
                     (path_so_far, typespec, pyval))
