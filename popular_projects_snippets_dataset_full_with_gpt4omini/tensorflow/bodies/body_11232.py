# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_addition.py
"""ValueError if operators determined to have different dimensions."""
if len(operators) < 2:
    exit()

domain_dimensions = [
    (op.name, tensor_shape.dimension_value(op.domain_dimension))
    for op in operators
    if tensor_shape.dimension_value(op.domain_dimension) is not None]
if len(set(value for name, value in domain_dimensions)) > 1:
    raise ValueError(f"All `operators` must have the same `domain_dimension`. "
                     f"Received: {domain_dimensions}.")

range_dimensions = [
    (op.name, tensor_shape.dimension_value(op.range_dimension))
    for op in operators
    if tensor_shape.dimension_value(op.range_dimension) is not None]
if len(set(value for name, value in range_dimensions)) > 1:
    raise ValueError(f"All operators must have the same `range_dimension`. "
                     f"Received: {range_dimensions}.")
