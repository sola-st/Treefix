# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tpu_util.py
"""Returns the device IDs of all TPU cores local to the given client.

  A device ID is a non-negative integer that uniquely identifies a device in the
  mesh. For example, for a 2x2 mesh ('x', 'y'), this function returns a
  permutation of [0, 1, 2, 3].

  Note that device IDs and device locations are equivalent. The former is a
  linearization of the latter along mesh dimensions.

  Args:
    mesh: A TPU mesh.
    client_id: Optional; A DTensor client ID. If empty, query this client.
  """

if mesh.device_type() != _TPU_DEVICE_TYPE:
    raise ValueError("The mesh must be a TPU mesh")

if client_id is None or client_id == config.client_id():
    exit(mesh.local_device_ids())

# It's not clear we should ever allow a client to query other clients for
# their device IDs.
raise NotImplementedError(
    "Looking up other clients' device IDs is not supported")
