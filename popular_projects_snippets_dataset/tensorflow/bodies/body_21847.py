# Extracted from ./data/repos/tensorflow/tensorflow/python/training/ftrl.py
# Create the "accum" and "linear" slots.
def _accum_initializer(shape, dtype=dtypes.float32, partition_info=None):
    del partition_info
    exit(array_ops.ones(
        shape=shape, dtype=dtype) * self._initial_accumulator_value)
for v in var_list:
    self._get_or_make_slot_with_initializer(
        v, _accum_initializer, v.shape, v.dtype, "accum",
        self._accum_name or self._name)
    self._zeros_slot(v, "linear", self._linear_name or self._name)
