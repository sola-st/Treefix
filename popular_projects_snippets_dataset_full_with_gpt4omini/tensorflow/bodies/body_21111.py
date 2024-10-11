# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad.py
for v in var_list:
    dtype = v.dtype.base_dtype
    if v.get_shape().is_fully_defined():
        init = init_ops.constant_initializer(self._initial_accumulator_value,
                                             dtype=dtype)
    else:
        init = self._init_constant_op(v, dtype)
    self._get_or_make_slot_with_initializer(v, init, v.get_shape(), dtype,
                                            "accumulator", self._name)
