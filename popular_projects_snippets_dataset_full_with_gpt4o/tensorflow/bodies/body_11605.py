# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Recursively converts ResourceVariables in the LinearOperator to Tensors.

    The usage of `self._type_spec._from_components` violates the contract of
    `CompositeTensor`, since it is called on a different nested structure
    (one containing only `Tensor`s) than `self.type_spec` specifies (one that
    may contain `ResourceVariable`s). Since `LinearOperator`'s
    `_from_components` method just passes the contents of the nested structure
    to `__init__` to rebuild the operator, and any `LinearOperator` that may be
    instantiated with `ResourceVariables` may also be instantiated with
    `Tensor`s, this usage is valid.

    Returns:
      tensor_operator: `self` with all internal Variables converted to Tensors.
    """
# pylint: disable=protected-access
components = self._type_spec._to_components(self)
tensor_components = variable_utils.convert_variables_to_tensors(
    components)
exit(self._type_spec._from_components(tensor_components))
