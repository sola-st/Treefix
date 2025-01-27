# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
"""Register overloads for all operators."""
for operator in ops.Tensor.OVERLOADABLE_OPERATORS:
    if operator == '__getitem__':
        continue

    cls._overload_operator(operator)
