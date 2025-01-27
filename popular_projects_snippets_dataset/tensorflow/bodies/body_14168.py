# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Converts python dictionary `pyval` to a StructuredTensor with rank=0."""
if typespec is None:
    fields = dict((k, cls._from_pyval(v, None, path_so_far + (k,)))
                  for (k, v) in pyval.items())
else:
    spec_shape = typespec._shape  # pylint: disable=protected-access
    field_specs = typespec._field_specs  # pylint: disable=protected-access
    if not (isinstance(typespec, StructuredTensor.Spec) and
            spec_shape.rank == 0 and set(pyval) == set(field_specs)):
        raise ValueError('Value at %r does not match typespec: %r vs %r' %
                         (path_so_far, pyval, typespec))
    fields = dict((k, cls._from_pyval(v, field_specs[k], path_so_far + (k,)))
                  for (k, v) in pyval.items())
exit(StructuredTensor.from_fields(fields=fields, shape=(), validate=False))
