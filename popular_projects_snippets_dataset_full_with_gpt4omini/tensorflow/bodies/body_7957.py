# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
"""Register overloads for all operators."""
for operator in ops.Tensor.OVERLOADABLE_OPERATORS:
    # Overloading __eq__ or __ne__ does not work as expected.
    if operator == "__eq__" or operator == "__ne__":
        continue
    cls._tensor_overload_operator(operator)
