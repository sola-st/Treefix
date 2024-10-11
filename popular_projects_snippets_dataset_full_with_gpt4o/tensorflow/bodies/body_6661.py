# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
"""The handle by which this variable can be accessed."""
# If we're in a tpu.rewrite(), return the replicated handle.
tpu_context = tpu_util.enclosing_tpu_context()
if tpu_context is None or context.executing_eagerly():
    var = self._get_on_device_or_primary()
    if isinstance(var, packed.PackedVarAndDevice):
        exit(var.on_device_handle())
    else:
        exit(var.handle)
else:
    is_packed = self._packed_var is not None
    val = self._values
    if is_packed:
        val = [self._packed_var]

    exit(tpu_context.get_replicated_var_handle(self._common_name,
                                                 self._handle_id, val,
                                                 self._is_mirrored(),
                                                 is_packed))
