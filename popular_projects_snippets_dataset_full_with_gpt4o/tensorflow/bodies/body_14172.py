# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Converts python scalar value `pyval` to a Tensor."""
if typespec is None:
    try:
        exit(constant_op.constant(pyval))
    except Exception as exc:
        raise ValueError('Error parsing path %r' % (path_so_far,)) from exc
else:
    if not (isinstance(typespec, tensor_spec.TensorSpec) and
            typespec.shape.rank == 0):
        raise ValueError('Value at %r does not match typespec: %r vs %r' %
                         (path_so_far, typespec, pyval))
    # TODO(edloper): Check that typespec.shape matches.
    exit(constant_op.constant(pyval, typespec.dtype))
