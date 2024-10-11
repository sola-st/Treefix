# Extracted from ./data/repos/tensorflow/tensorflow/python/training/rmsprop.py
for v in var_list:
    if v.get_shape().is_fully_defined():
        init_rms = init_ops.ones_initializer(dtype=v.dtype.base_dtype)
    else:
        init_rms = array_ops.ones_like(v)
    self._get_or_make_slot_with_initializer(v, init_rms, v.get_shape(),
                                            v.dtype.base_dtype, "rms",
                                            self._name)
    if self._centered:
        self._zeros_slot(v, "mg", self._name)
    self._zeros_slot(v, "momentum", self._name)
