# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Register overloads for all operators."""
for operator in ops.Tensor.OVERLOADABLE_OPERATORS:
    cls._OverloadOperator(operator)
# For slicing, bind getitem differently than a tensor (use SliceHelperVar
# instead)
# pylint: disable=protected-access
setattr(cls, "__getitem__", array_ops._SliceHelperVar)
