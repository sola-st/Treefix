# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Ensures integers remain unaffected despite casting to/from int/float types.

  Example integer-types: `uint8`, `int32`, `bool`.
  Example floating-types: `float32`, `float64`.

  The largest possible integer representable by an IEEE754 floating-point is
  `2**(1 + mantissa_bits)` yet the largest possible integer as an int-type is
  `2**(bits - 1) - 1`. This function ensures that a `Tensor` purporting to have
  integer-form values can be cast to some other type without loss of precision.

  The smallest representable integer is the negative of the largest
  representable integer, except for types: `uint8`, `uint16`, `bool`. For these
  types, the smallest representable integer is `0`.

  Args:
    x: `Tensor` representing integer-form values.
    target_dtype: TF `dtype` under which `x` should have identical values.
    assert_nonnegative: `bool` indicating `x` should contain nonnegative values.
    name: A name for this operation (optional).

  Returns:
    x: Input `Tensor` with appropriate assertions embedded.

  Raises:
    TypeError: if `x` is neither integer- nor floating-type.
    TypeError: if `target_dtype` is neither integer- nor floating-type.
    TypeError: if neither `x` nor `target_dtype` are integer-type.
  """

with ops.name_scope(name, values=[x]):
    x = ops.convert_to_tensor(x, name="x")
    if (not _is_integer_like_by_dtype(x.dtype) and not x.dtype.is_floating):
        raise TypeError("{}.dtype must be floating- or "
                        "integer-type.".format(x.dtype.name))
    if (not _is_integer_like_by_dtype(target_dtype) and
        not target_dtype.is_floating):
        raise TypeError("target_dtype ({}) must be floating- or "
                        "integer-type.".format(target_dtype.name))
    if (not _is_integer_like_by_dtype(x.dtype) and
        not _is_integer_like_by_dtype(target_dtype)):
        raise TypeError("At least one of {}.dtype ({}) and target_dtype ({}) "
                        "must be integer-type.".format(x, x.dtype.name,
                                                       target_dtype.name))

    assertions = []
    if assert_nonnegative:
        assertions += [
            check_ops.assert_non_negative(
                x, message="Elements must be non-negative."),
        ]

    if x.dtype.is_floating:
        # Being here means _is_integer_like_by_dtype(target_dtype) = True.
        # Since this check implies the magnitude check below, we need only it.
        assertions += [
            assert_integer_form(
                x,
                int_dtype=target_dtype,
                message="Elements must be {}-equivalent.".format(
                    target_dtype.name)),
        ]
    else:
        if (_largest_integer_by_dtype(x.dtype) >
            _largest_integer_by_dtype(target_dtype)):
            # Cast may lose integer precision.
            assertions += [
                check_ops.assert_less_equal(
                    x,
                    _largest_integer_by_dtype(target_dtype),
                    message=("Elements cannot exceed {}.".format(
                        _largest_integer_by_dtype(target_dtype)))),
            ]
        if (not assert_nonnegative and (_smallest_integer_by_dtype(
            x.dtype) < _smallest_integer_by_dtype(target_dtype))):
            assertions += [
                check_ops.assert_greater_equal(
                    x,
                    _smallest_integer_by_dtype(target_dtype),
                    message=("Elements cannot be smaller than {}.".format(
                        _smallest_integer_by_dtype(target_dtype)))),
            ]

    if not assertions:
        exit(x)
    exit(control_flow_ops.with_dependencies(assertions, x))
