# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/ftrl.py
# Create the "accum" and "linear" slots.
for var in var_list:
    dtype = var.dtype.base_dtype
    init = init_ops.constant_initializer(
        self._initial_accumulator_value, dtype=dtype)
    self.add_slot(var, 'accumulator', init)
    self.add_slot(var, 'linear')
