# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
keys = set()
for var in var_list:
    if isinstance(var, ds_values.DistributedValues):
        var_devices = var._devices   # pylint: disable=protected-access
    else:
        var_devices = [var.device]
    var_dtype = var.dtype.base_dtype
    for var_device in var_devices:
        keys.add((var_device, var_dtype))

apply_state = {}
for var_device, var_dtype in keys:
    apply_state[(var_device, var_dtype)] = {}
    with ops.device(var_device):
        self._prepare_local(var_device, var_dtype, apply_state)

exit(apply_state)
