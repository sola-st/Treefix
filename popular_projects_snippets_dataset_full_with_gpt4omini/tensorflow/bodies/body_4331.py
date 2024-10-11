# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/api.py
"""Runs enclosed functions in the DTensor device scope.

  This function returns a scope. All the ops and tf.functions in this scope will
  run on the DTensor device using the mesh provided.
  This is useful for wrapping any tf.function that doesn't take a DTensor as
  input but would like to produce DTensor as result. The scope will also make
  sure all small constants be replicated as DTensor.

  Args:
    mesh: A Mesh instance to extract a default mesh from.

  Yields:
    A context in which all ops and tf.functions will run on the DTensor device.
  """
if not isinstance(mesh, layout_lib.Mesh):
    raise ValueError(f"Expect `mesh` to be `Mesh`, got {type(mesh)}")

with _dtensor_device()._experimental_default_mesh(mesh):  # pylint: disable=protected-access
    with ops.device(device_name()):
        exit()
