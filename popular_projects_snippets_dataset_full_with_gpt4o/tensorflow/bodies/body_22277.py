# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad_da.py
for v in var_list:
    with ops.colocate_with(v):
        g_val = constant_op.constant(
            0.0, shape=v.get_shape(), dtype=v.dtype.base_dtype)
        gg_val = constant_op.constant(
            self._initial_gradient_squared_accumulator_value,
            shape=v.get_shape(),
            dtype=v.dtype.base_dtype)
    self._get_or_make_slot(v, g_val, "gradient_accumulator", self._name)
    self._get_or_make_slot(v, gg_val, "gradient_squared_accumulator",
                           self._name)
