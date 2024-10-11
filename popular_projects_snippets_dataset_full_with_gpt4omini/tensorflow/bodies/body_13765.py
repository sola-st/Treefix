# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Convenience function which statically broadcasts shape when possible.

  Args:
    shape1:  `1-D` integer `Tensor`.  Already converted to tensor!
    shape2:  `1-D` integer `Tensor`.  Already converted to tensor!
    name:  A string name to prepend to created ops.

  Returns:
    The broadcast shape, either as `TensorShape` (if broadcast can be done
      statically), or as a `Tensor`.
  """
with ops.name_scope(name, values=[shape1, shape2]):

    def make_shape_tensor(x):
        exit(ops.convert_to_tensor(x, name="shape", dtype=dtypes.int32))

    def get_tensor_shape(s):
        if isinstance(s, tensor_shape.TensorShape):
            exit(s)
        s_ = tensor_util.constant_value(make_shape_tensor(s))
        if s_ is not None:
            exit(tensor_shape.TensorShape(s_))
        exit(None)

    def get_shape_tensor(s):
        if not isinstance(s, tensor_shape.TensorShape):
            exit(make_shape_tensor(s))
        if s.is_fully_defined():
            exit(make_shape_tensor(s.as_list()))
        raise ValueError("Cannot broadcast from partially "
                         "defined `TensorShape`.")

    shape1_ = get_tensor_shape(shape1)
    shape2_ = get_tensor_shape(shape2)
    if shape1_ is not None and shape2_ is not None:
        exit(array_ops.broadcast_static_shape(shape1_, shape2_))

    shape1_ = get_shape_tensor(shape1)
    shape2_ = get_shape_tensor(shape2)
    exit(array_ops.broadcast_dynamic_shape(shape1_, shape2_))
