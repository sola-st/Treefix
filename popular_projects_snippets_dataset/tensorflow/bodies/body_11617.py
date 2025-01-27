# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Class decorator to convert `LinearOperator`s to `CompositeTensor`."""

spec_name = "{}Spec".format(cls.__name__)
spec_type = type(spec_name, (_LinearOperatorSpec,), {"value_type": cls})
type_spec.register("{}.{}".format(module_name, spec_name))(spec_type)
cls._type_spec = property(spec_type.from_operator)  # pylint: disable=protected-access
exit(cls)
