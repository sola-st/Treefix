# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/hdf5_format.py
"""Saves the weights of a list of layers to a HDF5 group.

  Args:
      f: HDF5 group.
      layers: List of layer instances.
  """
from tensorflow.python.keras import __version__ as keras_version  # pylint: disable=g-import-not-at-top

save_attributes_to_hdf5_group(
    f, 'layer_names', [layer.name.encode('utf8') for layer in layers])
f.attrs['backend'] = backend.backend().encode('utf8')
f.attrs['keras_version'] = str(keras_version).encode('utf8')

# Sort model layers by layer name to ensure that group names are strictly
# growing to avoid prefix issues.
for layer in sorted(layers, key=lambda x: x.name):
    g = f.create_group(layer.name)
    weights = _legacy_weights(layer)
    weight_values = backend.batch_get_value(weights)
    weight_names = [w.name.encode('utf8') for w in weights]
    save_attributes_to_hdf5_group(g, 'weight_names', weight_names)
    for name, val in zip(weight_names, weight_values):
        param_dset = g.create_dataset(name, val.shape, dtype=val.dtype)
        if not val.shape:
            # scalar
            param_dset[()] = val
        else:
            param_dset[:] = val
