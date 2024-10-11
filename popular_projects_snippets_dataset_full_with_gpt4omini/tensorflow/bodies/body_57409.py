# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Add a given index into the function structure."""
if sort is None:
    stuff[index] = _LiteSingleOperand(operand)
else:
    if index not in stuff:
        stuff[index] = _LiteAggregateOperand(aggregation)
    stuff[index].add(sort, operand)
