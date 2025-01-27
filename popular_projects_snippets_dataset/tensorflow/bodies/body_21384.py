# Extracted from ./data/repos/tensorflow/tensorflow/python/training/proximal_adagrad.py
for v in var_list:
    with ops.colocate_with(v):
        val = constant_op.constant(self._initial_accumulator_value,
                                   shape=v.get_shape(),
                                   dtype=v.dtype.base_dtype)
    self._get_or_make_slot(v, val, "accumulator", self._name)
