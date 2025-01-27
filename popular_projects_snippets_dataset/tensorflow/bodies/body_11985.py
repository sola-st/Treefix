# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/state_ops.py
"""Initializes variable with "init".

  This op does the following:
  if init is a Tensor, v = init
  if callable(init): v = init(VariableShape(v), v.dtype)

  Args:
    v: Variable to initialize
    init: Tensor to assign to v,
      Or an object convertible to Tensor e.g. nparray,
      Or an Initializer that generates a tensor given the shape and type of v.
      An "Initializer" is a callable that returns a tensor that "v" should be
      set to. It will be called as init(shape, dtype).
    name: Optional name for the op.

  Returns:
    The operation that initializes v.
  """
with ops.name_scope(None, v.op.name + "/", [v, init]):
    with ops.name_scope(name) as scope:
        with ops.colocate_with(v):
            if callable(init):
                assert v.get_shape().is_fully_defined(), "Variable shape unknown."
                # TODO(mrry): Convert to v.shape when the property and
                # accessor are reconciled (and all initializers support
                # tf.TensorShape objects).
                value = init(v.get_shape().as_list(), v.dtype.base_dtype)
                value = ops.convert_to_tensor(value, name="value")
                exit(gen_state_ops.assign(v, value, name=scope))
            else:
                init = ops.convert_to_tensor(init, name="init")
                exit(gen_state_ops.assign(v, init, name=scope))
