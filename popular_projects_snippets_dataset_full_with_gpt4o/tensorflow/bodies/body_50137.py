# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/hdf5_format.py
"""Saves optimizer weights of a optimizer to a HDF5 group.

  Args:
      hdf5_group: HDF5 group.
      optimizer: optimizer instance.
  """

symbolic_weights = getattr(optimizer, 'weights')
if symbolic_weights:
    weights_group = hdf5_group.create_group('optimizer_weights')
    weight_names = [str(w.name).encode('utf8') for w in symbolic_weights]
    save_attributes_to_hdf5_group(weights_group, 'weight_names', weight_names)
    weight_values = backend.batch_get_value(symbolic_weights)
    for name, val in zip(weight_names, weight_values):
        param_dset = weights_group.create_dataset(
            name, val.shape, dtype=val.dtype)
        if not val.shape:
            # scalar
            param_dset[()] = val
        else:
            param_dset[:] = val
