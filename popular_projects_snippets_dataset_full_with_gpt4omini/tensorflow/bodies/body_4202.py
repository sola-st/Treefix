# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tpu_util.py
"""Returns the device locations of all TPU cores local to the given client.

  A device location is a dictionary from dimension names to indices on those
  dimensions. For example, for a 2x2 mesh ('x', 'y'), this function returns a
  permutation of this list:

    [{'x': 0, 'y': 0},
     {'x': 0, 'y': 1},
     {'x': 1, 'y': 0},
     {'x': 1, 'y': 1}].

  Note that device IDs and device locations are equivalent. The former is a
  linearization of the latter along mesh dimensions.

  Args:
    mesh: A TPU mesh.
    client_id: Optional; A DTensor client ID. If empty, query this client.
  """

if mesh.device_type() != _TPU_DEVICE_TYPE:
    raise ValueError("The mesh must be a TPU mesh")

if client_id is None or client_id == config.client_id():
    exit(mesh.local_device_locations())

# It's not clear we should ever allow a client to query other clients for
# their device locations.
raise NotImplementedError(
    "Looking up other clients' device locations is not supported")
