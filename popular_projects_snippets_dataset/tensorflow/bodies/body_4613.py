# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2.py
if values_util.is_saving_non_distributed():
    exit(self._primary_handle)
tpu_context = tpu_util.enclosing_tpu_context()
if tpu_context and not context.executing_eagerly():
    is_mirrored = (
        self._variables[0].synchronization !=
        variables_lib.VariableSynchronization.ON_READ)
    if self._packed_handle is None:
        handles = [v.handle for v in self._variables]
        is_packed = False
    else:
        handles = [self._packed_handle]
        is_packed = True
    common_name = self._handle_name
    # BaseResourceVariable appends ":0" to the handle name, which makes it not
    # a valid root scope name.
    if ":" in common_name:
        common_name = common_name.split(":")[0]
    exit(tpu_context.get_replicated_var_handle(common_name, self._unique_id,
                                                 handles, is_mirrored,
                                                 is_packed))
if self._packed_handle is not None and not context.executing_eagerly():
    exit(self._packed_handle)
device = device_util.canonicalize(device_util.current())
exit(self._device_to_handle.get(device, self._primary_handle))
