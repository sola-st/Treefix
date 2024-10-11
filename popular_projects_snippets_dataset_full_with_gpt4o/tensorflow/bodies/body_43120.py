# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
"""Register overloads for all operators."""
for operator in ops.Tensor.OVERLOADABLE_OPERATORS:
    cls._overload_operator(operator)
