# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/hdf5_format.py
"""Implements topological (order-based) weight loading.

  Args:
      f: A pointer to a HDF5 group.
      layers: a list of target layers.

  Raises:
      ValueError: in case of mismatch between provided layers
          and weights file.
  """
if 'keras_version' in f.attrs:
    original_keras_version = f.attrs['keras_version']
    if hasattr(original_keras_version, 'decode'):
        original_keras_version = original_keras_version.decode('utf8')
else:
    original_keras_version = '1'
if 'backend' in f.attrs:
    original_backend = f.attrs['backend']
    if hasattr(original_backend, 'decode'):
        original_backend = original_backend.decode('utf8')
else:
    original_backend = None

filtered_layers = []
for layer in layers:
    weights = _legacy_weights(layer)
    if weights:
        filtered_layers.append(layer)

layer_names = load_attributes_from_hdf5_group(f, 'layer_names')
filtered_layer_names = []
for name in layer_names:
    g = f[name]
    weight_names = load_attributes_from_hdf5_group(g, 'weight_names')
    if weight_names:
        filtered_layer_names.append(name)
layer_names = filtered_layer_names
if len(layer_names) != len(filtered_layers):
    raise ValueError('You are trying to load a weight file '
                     'containing ' + str(len(layer_names)) +
                     ' layers into a model with ' + str(len(filtered_layers)) +
                     ' layers.')

# We batch weight value assignments in a single backend call
# which provides a speedup in TensorFlow.
weight_value_tuples = []
for k, name in enumerate(layer_names):
    g = f[name]
    weight_names = load_attributes_from_hdf5_group(g, 'weight_names')
    weight_values = [np.asarray(g[weight_name]) for weight_name in weight_names]
    layer = filtered_layers[k]
    symbolic_weights = _legacy_weights(layer)
    weight_values = preprocess_weights_for_loading(
        layer, weight_values, original_keras_version, original_backend)
    if len(weight_values) != len(symbolic_weights):
        raise ValueError('Layer #' + str(k) + ' (named "' + layer.name +
                         '" in the current model) was found to '
                         'correspond to layer ' + name + ' in the save file. '
                         'However the new layer ' + layer.name + ' expects ' +
                         str(len(symbolic_weights)) +
                         ' weights, but the saved weights have ' +
                         str(len(weight_values)) + ' elements.')
    weight_value_tuples += zip(symbolic_weights, weight_values)
backend.batch_set_value(weight_value_tuples)
