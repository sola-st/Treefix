# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource.py
"""Initialize the `TrackableResource`.

    Args:
      device: A string indicating a required placement for this resource,
        e.g. "CPU" if this resource must be created on a CPU device. A blank
        device allows the user to place resource creation, so generally this
        should be blank unless the resource only makes sense on one device.
    """
global _RESOURCE_TRACKER_STACK
for resource_tracker in _RESOURCE_TRACKER_STACK:
    resource_tracker.add_resource(self)
super().__init__(device=device)
