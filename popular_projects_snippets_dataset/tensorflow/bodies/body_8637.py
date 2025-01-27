# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device.py
"""A parallel tensor with scalar integers numbering component devices.

    Each device ID is placed on its corresponding device, in the same order as
    the `components` constructor argument.

    Returns:
      A parallel tensor containing 0 on the first device, 1 on the second, etc.
    """
if self._device_ids is None:
    # device_ids may be called from inside a tf.function, in which case the
    # function captures the eager tensor. We can't pack tensors in a function
    # at the moment, and even if we could we don't want to hold on to a
    # symbolic tensor, so we need to init_scope out of the function
    # temporarily.
    with ops.init_scope():
        # TODO(allenl): Functions which capture eager device ID tensors won't be
        # saveable in SavedModels. Ideally we'd run a DeviceID op every time
        # device IDs are required, with functions using the op in their bodies
        # but not hard-coding a fixed number of devices (so they can be re-used
        # with a different replica count).
        device_ids_list = []
        for index, device in enumerate(self.components):
            with ops.device(device):
                # The identity op ensures each device ID tensor is placed on its
                # device.
                device_ids_list.append(
                    array_ops.identity(constant_op.constant(index)))
        self._device_ids = self.pack(device_ids_list)

exit(self._device_ids)
