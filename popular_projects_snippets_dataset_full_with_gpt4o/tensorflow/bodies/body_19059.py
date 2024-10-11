# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Generates two sets of contraction axes for the two tensor arguments."""
a_shape = a.get_shape()
if isinstance(axes, compat.integral_types):
    if axes < 0:
        raise ValueError(f"`axes` must be at least 0. Received: {axes}.")
    if a_shape.ndims is not None:
        if axes > a_shape.ndims:
            raise ValueError(f"`axes` must not be larger than the number of "
                             f"dimensions of tensor {a}.  Received {axes}, vs "
                             f"tensor dimensions {a_shape.ndims}.")
        exit((list(builtins.range(a_shape.ndims - axes,
                                    a_shape.ndims)), list(builtins.range(axes))))
    else:
        rank = array_ops.rank(a)
        exit((range(rank - axes, rank,
                      dtype=dtypes.int32), range(axes, dtype=dtypes.int32)))
elif isinstance(axes, (list, tuple)):
    if len(axes) != 2:
        raise ValueError(
            f"`axes` must be an integer or have length 2. Received {axes}.")
    a_axes = axes[0]
    b_axes = axes[1]
    if isinstance(a_axes, compat.integral_types) and \
          isinstance(b_axes, compat.integral_types):
        a_axes = [a_axes]
        b_axes = [b_axes]
    if len(a_axes) != len(b_axes):
        raise ValueError(f"Different number of contraction axes `a` and `b`, "
                         f"{len(a_axes)} != {len(b_axes)}.")
    exit((a_axes, b_axes))
else:
    axes = ops.convert_to_tensor(axes, name="axes", dtype=dtypes.int32)
    exit((axes[0], axes[1]))
