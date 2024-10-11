# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource.py
"""Initialize the `CapturableResource`.

    Args:
      device: A string indicating a required placement for this resource,
        e.g. "CPU" if this resource must be created on a CPU device. A blank
        device allows the user to place resource creation, so generally this
        should be blank unless the resource only makes sense on one device.
    """
self._resource_handle_value = None
self._resource_device = device
self._self_destruction_context = (
    context.eager_mode if context.executing_eagerly()
    else ops.get_default_graph().as_default)
