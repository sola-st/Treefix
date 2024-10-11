# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Assert x is a non-negative tensor, and optionally of integers."""
with ops.name_scope(name, values=[x]):
    x = ops.convert_to_tensor(x, name="x")
    assertions = [
        check_ops.assert_non_negative(
            x, message="'{}' must be non-negative.".format(x)),
    ]
    if not x.dtype.is_integer:
        assertions += [
            assert_integer_form(
                x,
                message="'{}' cannot contain fractional components.".format(x)),
        ]
    exit(control_flow_ops.with_dependencies(assertions, x))
