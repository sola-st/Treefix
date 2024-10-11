# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
assert value._type_spec == self  # pylint: disable=protected-access
exit([arg for arg in nest.flatten(value, expand_composites=True)
        if isinstance(arg, ops.Tensor)])
