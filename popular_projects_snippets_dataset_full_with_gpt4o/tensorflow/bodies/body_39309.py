# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver.py
"""Specify a list of `SaveableObject`s to save and restore.

    Args:
      serialized_tensors: A dictionary mapping `Trackable` to a tensor dict,
        which maps checkpoint_key -> (slice_spec ->) -> Tensor/SaveSpec. The
        `Trackable` key is used to get the `restore_from_tensors` function,
        and may be `None` if the tensor is not meant to be restored.
      registered_savers: A dictionary mapping `registration.RegisteredSaver`
        namedtuples to a dictionary of named Trackables. The keys of the
        Trackable dictionary are string names that uniquely identify the
        Trackable in the checkpoint.
      call_with_mapped_captures: TODO
    """
# Keep these two data structures so that we can map restored tensors to
# the Trackable restore functions.
self._keys_to_restore_fn = {}
self._restore_fn_to_keys = {}

# Extract serialized tensors and separate by device.
tensors_by_device = {}  # device -> checkpoint key -> (slice_spec ->) tensor

for obj, tensor_dict in serialized_tensors.items():
    restore_fn = _restore_noop if obj is None else obj._restore_from_tensors

    # Divide tensor_dict by device.
    for checkpoint_key, maybe_tensor in tensor_dict.items():
        if not isinstance(maybe_tensor, dict):
            # Make sure that maybe_tensor is structured as {slice_spec -> tensor}.
            maybe_tensor = {"": maybe_tensor}

        for slice_spec, tensor in maybe_tensor.items():
            if (checkpoint_key, slice_spec) in self._keys_to_restore_fn:
                raise ValueError(
                    "Recieved multiple tensors with the same checkpoint key and "
                    "slice spec. This is invalid because one will overwrite the "
                    "other in the checkpoint. This indicates a bug in the "
                    "Checkpoint key-generation.")
            self._keys_to_restore_fn[(checkpoint_key, slice_spec)] = restore_fn
            self._restore_fn_to_keys.setdefault(restore_fn, []).append(
                (checkpoint_key, slice_spec))

            host_device = saveable_object_util.set_cpu0(tensor.device)
            (tensors_by_device
             .setdefault(host_device, {})
             .setdefault(checkpoint_key, {})[slice_spec]) = tensor
self._single_device_savers = {
    device: _SingleDeviceSaver(tensor_slice_dict)
    for device, tensor_slice_dict in tensors_by_device.items()}

self._registered_savers = {}
if registered_savers:
    for registered_name, trackables in registered_savers.items():
        save_fn = _get_mapped_registered_save_fn(
            registration.get_save_function(registered_name),
            trackables, call_with_mapped_captures)
        restore_fn = _get_mapped_registered_restore_fn(
            registration.get_restore_function(registered_name),
            trackables, call_with_mapped_captures)
        self._registered_savers[registered_name] = (save_fn, restore_fn)
