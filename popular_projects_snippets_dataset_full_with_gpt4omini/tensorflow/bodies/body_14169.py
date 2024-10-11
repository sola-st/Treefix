# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Converts python list `pyval` to a StructuredTensor with rank>1."""
fields = dict((key, []) for key in keys)
for child in pyval:
    _pyval_update_fields(child, fields, 1)
if typespec is None:
    shape = tensor_shape.TensorShape([None] * rank)
    for (key, target) in fields.items():
        fields[key] = cls._from_pyval(target, None, path_so_far + (key,))
else:
    field_specs = typespec._fields  # pylint: disable=protected-access
    if ((not isinstance(typespec, StructuredTensor.Spec)) or  # pylint: disable=superfluous-parens
        (set(fields) - set(field_specs))):
        raise ValueError('Value at %r does not match typespec: %r vs %r' %
                         (path_so_far, pyval, typespec))
    shape = typespec._shape
    if shape.rank < rank:
        raise ValueError('Value at %r does not match typespec (rank mismatch): '
                         '%r vs %r' % (path_so_far, pyval, typespec))
    for (key, spec) in field_specs.items():
        fields[key] = cls._from_pyval(
            fields.get(key, []), spec, path_so_far + (key,))
try:
    if not fields and typespec is None:
        # TODO(b/183245576): handle cases where the typespec is known
        # but the dictionary is empty.
        exit(StructuredTensor._from_pylist_of_empty_dict(pyval, rank))
    exit(StructuredTensor.from_fields(
        fields=fields, shape=shape, validate=False))
except Exception as exc:
    raise ValueError('Error parsing path %r' % (path_so_far,)) from exc
