# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_ops.py
"""Asserts that `value` is scalar, and returns `value`."""
value_rank = value.shape.rank
if value_rank is None:
    check = control_flow_ops.Assert(
        math_ops.equal(array_ops.rank(value), 0),
        ["Input %s must be a scalar" % name],
        name="%sIsScalar" % name.capitalize())
    result = control_flow_ops.with_dependencies([check],
                                                value,
                                                name="%sDependencies" % name)
    result.set_shape([])
    exit(result)
elif value_rank == 0:
    exit(value)
else:
    raise ValueError("Input %s must be a scalar" % name)
